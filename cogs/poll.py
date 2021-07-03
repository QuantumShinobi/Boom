import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import re
import discord


class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @has_permissions(administrator=True, manage_guild=True)
    async def poll(self, ctx):
        await ctx.send("Enter the topic of the poll")
        try:
            title = await self.bot.wait_for(
                "message", timeout=30, check=lambda message: message.author.id == ctx.author.id)
        except asyncio.TimeoutError:
            return await ctx.send("Timeout")
        else:
            await ctx.send('''
How long should the poll last(duration in hrs)
For eg, if you want the poll to be for 2 hours, type 2
''')
            try:
                time = await self.bot.wait_for(
                    "message", timeout=30, check=lambda message: message.author.id == ctx.author.id)
            except asyncio.TimeoutError:
                return await ctx.send("Timeout")
            else:

                re_check = re.match(r'\d', str(time.content))

                if re_check:
                    await ctx.send("Which channel do you want to the poll to be in?")
                    try:
                        gw_channel = await self.bot.wait_for(
                            "message", timeout=30, check=lambda message: message.author.id == ctx.author.id)
                    except asyncio.TimeoutError:
                        return await ctx.send("Timeout")
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
                            await ctx.send("""
Okay, now type the emojis with which u want to react
For eg, if the emojis are 😇 and 😈
Type
`😇 😈`
                            """)
                            try:
                                reactions = await self.bot.wait_for("message", timeout=30, check=lambda msg: msg.author.id == ctx.author.id)
                            except asyncio.TimeoutError:
                                return await ctx.send("Timeout")
                            else:
                                reaction_list = reactions.content.split()

                                await ctx.send("Enter the content")
                                try:
                                    message = await self.bot.wait_for("message", timeout=30, check=lambda message: message.author.id == ctx.author.id)

                                except asyncio.TimeoutError:
                                    return await ctx.send("Timeout")
                                else:
                                    content = message.content
                                    await ctx.send("Creating poll")

                                    channel = self.bot.get_channel(
                                        858984166136610826)
                                    print(channel)
                                    await self.create_poll(title=title.content, content=content, channel_id=gw_channel_obj, reactions=reaction_list)

                        else:
                            return await ctx.send("Channel not found")

                else:
                    return await ctx.send("That doesnt seem to be a valid duration")

    @commands.command()
    async def create_poll(self, title, content, channel_id, reactions):
        embed = discord.Embed(
            title=title, description=content, color=discord.Color.blurple())

        msg = await channel_id.send(embed=embed)
        for reaction in reactions:
            await msg.add_reaction(reaction)
