import asyncio
import discord
from discord.ext import commands
from mongo import *


class RMTCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def register(self, ctx):
        await ctx.send("Please enter your name")
        try:
            name = await self.bot.wait_for("message", timeout=30)
            print(name)
        except asyncio.TimeoutError:
            return await ctx.send("The request to register has timed out. Kindly restart the process")
        else:
            if await register(name=str(name), id=ctx.author.id):
                await ctx.send("You have been registered as an RMTian")
            else:
                await ctx.send("You are already registered")
