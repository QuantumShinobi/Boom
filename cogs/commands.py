import asyncio
from discord.ext import commands, tasks
from mongo import *
import pytz
from datetime import datetime
from .messages.dms import *


class RMTCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.send_dm.start()

    @commands.command(description="Register yourself as an RMTian")
    async def register(self, ctx):
        author = ctx.author
        if await RMTian.is_registered(id=author.id):
            return await ctx.send(f"{ctx.author.mention}, You are already registered")
        await ctx.send("Please enter your name")

        try:
            name = await self.bot.wait_for("message", timeout=30, check=lambda message: message.author == ctx.author)
        except asyncio.TimeoutError:
            return await ctx.send(f"{ctx.author.mention},The request to register has timed out. Kindly restart the process")
        else:
            if await register(name=str(name.content), id=ctx.author.id):
                await ctx.send(f"{ctx.author.mention}, you have been registered as an RMTian")
            else:
                await ctx.send(f"{ctx.author.mention}, you are already registered")

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
            await ctx.send(f"{ctx.author.mention}, you have been removed")
        else:
            await ctx.send("You are not registered")

    @commands.command(description="If you do not wish to recive DMs from the bot")
    async def nodms(self, ctx):
        if await RMTian.is_registered(id=ctx.author.id):
            await ctx.send("Ok wait")
        else:
            await ctx.send(f"Oof {ctx.author.mention}!, you need to be registered to run this command.")

    @tasks.loop(minutes=45)
    async def send_dm(self, *args, **kwargs):

        IST = pytz.timezone('Asia/Kolkata')

        now = datetime.now(tz=IST)
        time_before = now.replace(hour=13, minute=0, second=0, microsecond=0)
        time_after = now.replace(hour=15, minute=0, second=0, microsecond=0)
        if now > time_before and now < time_after:
            from mongo import collection
            for user in collection.find({"send_dm": True}):
                test_ids = [
                    765838723169386516, 764415588873273345, 795513154514714634]
                if user['discord_id'] in test_ids:
                    discord_user = self.bot.get_user(id=user['discord_id'])
                    print(f"Sending Dm to {discord_user}")
                    msg = await discord_user.send(ask(discord_user))
                    await msg.add_reaction("🇾")
                    await msg.add_reaction("🇳")

                    def check(reaction, user):
                        return reaction.emoji == "🇾" or reaction.emoji == "🇳" and user == discord_user
                    try:
                        reaction, r_user = await self.bot.wait_for("reaction_add", timeout=3600, check=check)
                    except asyncio.TimeoutError:
                        await discord_user.send("We didn't get any response from you")
                        file = open('coming.txt', mode="a+")
                        file.write(
                            f"No response from {discord_user.mention}\n")
                        file.close()
                    else:
                        await discord_user.send("Thank you for your response")
                        if reaction.emoji == "🇾":
                            file = open('coming.txt', mode="a+")
                            file.write(f"{r_user.mention} is coming down\n")
                            file.close()
                        elif reaction.emoji == "🇳":
                            file = open('coming.txt', mode="a+")
                            file.write(
                                f"{r_user.mention} is not coming down\n")
                            file.close()
                        else:
                            file = open('coming.txt', mode="a+")
                            file.write(
                                f"Didn't get a valid response from {r_user.mention}\n")
                            file.close()
            file = open("./coming.txt", mode="r")
            msg = ""
            for line in file.readlines():
                msg += line
            channel = self.bot.get_channel(866231728044507136)
            await channel.send(msg)
            file.close()
            # Delete all contents after sending DMs
            file = open('./coming.txt', mode='w')
            file.close()
            return True

    @send_dm.before_loop
    async def before_send_dm(self):
        print("Waiting for bot to get ready")
        await self.bot.wait_until_ready()
        print("Bot is ready")


def setup(bot: commands.Bot):
    bot.add_cog(RMTCommands(bot))
