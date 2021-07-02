import asyncio
import discord
from discord.ext import commands
from mongo import *


class RMTCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def register(self, ctx):
        author = ctx.author
        if await RMTian.is_registered(id=author.id):
            return ctx.send("You are already register")
        await ctx.send("Please enter your name")

        def check(u, *args, **kwargs):
            return u == author
        try:
            name = await self.bot.wait_for("message", timeout=30, check=lambda message: message.author == ctx.author)
            print(name.content)
        except asyncio.TimeoutError:
            return await ctx.send("The request to register has timed out. Kindly restart the process")
        else:
            if await register(name=str(name.content), id=ctx.author.id):
                await ctx.send("You have been registered as an RMTian")
            else:
                await ctx.send("You are already registered")

    @commands.command()
    async def remove(self, ctx):

        id = ctx.author.id
        if not await RMTian.is_registered(id=id):
            return ctx.send("You are not registered")
        await ctx.send("Type `yes` if you want to confirm your removal..")
        try:
            response = await self.bot.wait_for("message", timeout=30, check=lambda message: message.author == ctx.author)
            if response.content.lower() != "yes" and response.content.lower() != "no":
                return await ctx.send("You didn't enter a valid response, the process has been cancelled")
            elif response.content.lower() == "no":
                return await ctx.send("Okay, the process is cancelled")
        except asyncio.TimeoutError:
            return await ctx.send("No response was recieved, the process has been cancelled")
        if await remove_user(id):
            await ctx.send("You have been removed")
        else:
            await ctx.send("You are not registered")
