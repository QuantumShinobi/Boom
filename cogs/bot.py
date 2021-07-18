import discord
import datetime
from discord import Color
from discord.ext import commands, tasks
import sys
from .embeds import bot
from datetime import datetime
import pytz


class Bot(commands.Cog):
    """
    Basic bot functions
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        "Tells when the bot is ready"
        print("Bot is ready")
        channel = self.bot.get_channel(858296114415534100)
        other_channel = self.bot.get_channel(858984166136610826)
        await channel.send(embed=bot.ready_embed(sys.platform))
        await other_channel.send(embed=bot.ready_embed(sys.platform))
        IST = pytz.timezone('Asia/Kolkata')
        sent_dms = False

        now = datetime.now(tz=IST)
        time_before = now.replace(hour=20, minute=0, second=0, microsecond=0)
        time_after = now.replace(hour=23, minute=0, second=0, microsecond=0)
        if now > time_before and now < time_after and sent_dms == False:
            from mongo import collection
            for user in collection.find({}):
                test_ids = [795513154514714634, 764415588873273345]
                if user['discord_id'] in test_ids:
                    discord_user = self.bot.get_user(id=user['discord_id'])
                    # await discord_user.send("Testing boom bot")

        # ? Ping Fight
        # channel2= self.bot.get_channel(852102295373086720)
        # for i in range(100):
        #   await channel2.send ("<@795513154514714634>\n<@765838723169386516>\n<@725311886739898429>\n<@804587223877419032>")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        "Identifies and reports edited messages"
        channel = self.bot.get_channel(858296114415534100)
        if int(before.channel.id) == 858296114415534100 or before.author.bot == True or before.content == after.content:
            pass
        else:
            await channel.send(embed=bot.edit_msg(before, after))

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.bot.get_channel(858296114415534100)
        if int(message.channel.id) == 858296114415534100:
            pass
        else:
            await channel.send(embed=bot.del_msg(message))

    @commands.command()
    async def help(self, ctx, *args, **kwargs):
        """
        Help command for the bot
        """
        embed = discord.Embed(color=Color.blue(), url="https://github.com/IamEinstein/Boom",
                              title=f"Boom Bot help,\n here are the list of commands", timestamp=datetime.datetime.now())
        embed.add_field(name="b!register",
                        value="Type b!register if you want to get registered as an RMTian ", inline=True)
        await ctx.send(embed=embed)
