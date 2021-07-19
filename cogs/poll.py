import asyncio
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
import re
import discord
from .messages.poll import *
from datetime import datetime, timedelta
from utils.tz import IST, format_time
from mongo import PollModel, polls, collection
import logging
import traceback
# TODO:  Make tie mechanism for polls
# TODO:  Make "makepoll" command


class Poll(commands.Cog):
    """
    The Poll cog
    Everything related to polls goes here
    """

    def __init__(self, bot):
        self.bot = bot
        self.check_ended.start()

    @commands.command(pass_context=True)
    @has_permissions(administrator=True, manage_guild=True)
    async def poll(self, ctx):
        """
        The poll command.
        This is used to create polls in an interactive manner
        Another command (makepoll) can be used to make polls in one command
        """
        await ctx.send(topic_msg)
        try:
            title = await self.bot.wait_for(
                "message", timeout=30, check=lambda message: message.author.id == ctx.author.id)
        except asyncio.TimeoutError:
            return await ctx.send(timeout_message)
        else:
            await ctx.send(duration_message)
            try:
                time = await self.bot.wait_for(
                    "message", timeout=30, check=lambda message: message.author.id == ctx.author.id)
            except asyncio.TimeoutError:
                return await ctx.send(timeout_message)
            else:

                re_check = re.match(r'\d', str(time.content))

                if re_check:
                    await ctx.send(channel_message)
                    try:
                        gw_channel = await self.bot.wait_for(
                            "message", timeout=30, check=lambda message: message.author.id == ctx.author.id)
                    except asyncio.TimeoutError:
                        return await ctx.send(timeout_message)
                    else:

                        for channel in ctx.guild.channels:
                            if str(channel.mention) == str(gw_channel.content):
                                gw_channel_name = gw_channel.content[2:-2]
                                gw_channel_obj = channel
                                break
                            else:
                                gw_channel_name = None
                                continue

                        if gw_channel_name != None:
                            await ctx.send(react_message)
                            try:
                                reactions = await self.bot.wait_for("message", timeout=30, check=lambda msg: msg.author.id == ctx.author.id)
                            except asyncio.TimeoutError:
                                return await ctx.send(timeout_message)
                            else:
                                reaction_list = reactions.content.split()

                                await ctx.send("Enter the content")
                                try:
                                    message = await self.bot.wait_for("message", timeout=30, check=lambda message: message.author.id == ctx.author.id)

                                except asyncio.TimeoutError:
                                    return await ctx.send(timeout_message)
                                else:
                                    content = message.content

                                    await ctx.send("Creating poll")
                                    await self.create_poll(title=title.content, content=content, channel=gw_channel_obj, reactions=reaction_list, time=int(time.content), time_created=datetime.now(tz=IST))
                        else:
                            return await ctx.send("Channel not found")
                else:
                    return await ctx.send("That doesn't seem to be a valid duration")

    async def create_poll(self, title: str, content: str, channel, reactions: list, time: int, time_created: datetime):
        """
        Function for creating a poll and registering it in the database
        """
        time_to_end = timedelta(minutes=time) + time_created
        embed = discord.Embed(
            title=title, description=content, color=discord.Color.blurple())
        embed.set_footer(text=f"Ends at {format_time(time_to_end)}")
        msg = await channel.send(embed=embed)
        for i, reaction, in enumerate(reactions):
            globals()[f"reaction_list{i}"] = []
            await msg.add_reaction(reaction)

        poll = PollModel(title=title, content=content, reactions=reactions,
                         start_time=time_created, end_time=time_to_end, poll_id=msg.id, channel_id=channel.id)
        try:
            poll.commit()
        except Exception as e:
            logging.error(traceback.format_exc())
            return False
        else:
            return True

    @commands.command()
    async def testpoll(self, ctx):
        """
        A (temporary) testing command,
        used to test polls
        """
        if ctx.author.id == 764415588873273345:
            await self.create_poll(title="Test", content="oof", channel=ctx.channel, reactions=['🤣', '😔', '😈'], time=0.5, time_created=datetime.now(tz=IST))

    async def end_poll(self, poll: PollModel):
        """
        To end the poll which is past the end time
        """
        channel = self.bot.get_channel(poll['channel_id'])
        msg = await channel.fetch_message(poll['poll_id'])
        reactions = msg.reactions
        reaction_count = 0
        reaction_emoji = None
        # tie = False

        for reaction in reactions:
            if reaction.count > reaction_count:
                reaction_count = reaction.count
                reaction_emoji = reaction.emoji
            # elif reaction_count == reaction.count:

        if reaction_emoji:
            await msg.reply(f"{reaction_emoji} has won")
            poll['ended'] = True
            poll['winner'] = reaction_emoji
            poll['winner_reaction_count'] = reaction_count
            print(poll)
            polls.find_and_modify(query={
                                  "poll_id": poll['poll_id'], "channel_id": poll['channel_id']}, update={"$set": poll})

    @tasks.loop(seconds=45)
    async def check_ended(self):
        """
        Checks for ended polls
        """
        print("Checking for ended polls")
        ended_polls = await PollModel.check_ended_polls()
        if ended_polls:
            for ended_poll in ended_polls:
                await self.end_poll(poll=ended_poll)

    @check_ended.before_loop
    async def before_check_ended(self):
        "Makes sure that the bot is ready before it checks for ended polls"
        await self.bot.wait_until_ready()
