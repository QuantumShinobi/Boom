import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import re
import discord
from .messages.poll import *


class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @has_permissions(administrator=True, manage_guild=True)
    async def poll(self, ctx):
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
                                    await self.create_poll(title=title.content, content=content, channel_id=gw_channel_obj, reactions=reaction_list, time=int(time.content), ctx=ctx)

                        else:
                            return await ctx.send("Channel not found")

                else:
                    return await ctx.send("That doesn't seem to be a valid duration")

    async def create_poll(self, title: str, content: str, channel_id, reactions, time: int, ctx):
        embed = discord.Embed(
            title=title, description=content, color=discord.Color.blurple())

        msg = await channel_id.send(embed=embed)
        for reaction in reactions:
            await msg.add_reaction(reaction)

        def check(reaction, u):
            return reaction.message.id == msg.id and str(reaction.emoji) in reactions
        # await asyncio.sleep(time)
        while True:
            reaction, user = await self.bot.wait_for("reaction_add", check=check)
            if reaction:
                users = await reaction.users().flatten()
            print(user, users, reaction.emoji)
            await channel_id.send(await reaction.users().flatten())
