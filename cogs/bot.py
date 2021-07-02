import discord
import datetime
from discord import Color
from discord.ext import commands
import sys
from .embeds import bot


class Bot(commands.Cog):
    """
    Basic bot functions 
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        "Tells mods when the bot is ready"
        channel = self.bot.get_channel(858296114415534100)
        other_channel = self.bot.get_channel(858984166136610826)
        await channel.send(embed=bot.ready_embed(sys.platform))
        await other_channel.send(embed=bot.ready_embed(sys.platform))

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        "Identifies and reports edited messages"

        channel = self.bot.get_channel(858296114415534100)
        embed = discord.Embed(
            color=Color.blue(), url="https://github.com/IamEinstein/Boom", title=f"{before.author} edited a message", timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=before.author.avatar_url)
        embed.add_field(name="Original Message",
                        value=f'{before.content}', inline=False)
        embed.add_field(name="Edited Message",
                        value=f'{after.content}', inline=True)
        embed.add_field(
            name="Channel", value=f"{before.channel.mention}", inline=True)

        if int(before.channel.id) == 858296114415534100 or before.author.bot == True or before.content == after.content:
            pass
        else:
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.bot.get_channel(858296114415534100)
        if int(message.channel.id) == 858296114415534100:
            pass
        else:
            embed = discord.Embed(
                color=Color.blue(), url="https://github.com/IamEinstein/Boom", title=f"{message.author} deleted a message", timestamp=datetime.datetime.now())
            embed.set_thumbnail(url=message.author.avatar_url)

            embed.add_field(name="Message Content",
                            value=f'{message.content}', inline=False)
            embed.add_field(
                name="Channel", value=f"{message.channel.mention}", inline=True)

            await channel.send(embed=embed)

    @commands.command()
    async def help(self, ctx, *args, **kwargs):
        embed = discord.Embed(color=Color.blue(), url="https://github.com/IamEinstein/Boom",
                              title=f"Boom Bot help,\n here are the list of commands", timestamp=datetime.datetime.now())
        embed.add_field(name="b!register",
                        value="Type b!register if you want to get registered as an RMTian ", inline=True)
        await ctx.send(embed=embed)


# keep_alive()
# client.run(token)
