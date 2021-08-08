
# Mod channel id= 858296114415534100
# Test channel id =858984166136610826
# test_ids = [795513154514714634, 764415588873273345]
import discord
import os
from discord.ext import commands
import sys
from .messages.embeds import ready_embed, edit_msg, del_msg, dm_join_embed, leave_embed


class Bot(commands.Cog):
    """
    Basic bot setup
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        "Tells when the bot is ready"
        print("Bot is ready")
        channel = self.bot.get_channel(858296114415534100)
        other_channel = self.bot.get_channel(858984166136610826)
        await channel.send(embed=ready_embed(sys.platform))
        await other_channel.send(embed=ready_embed(sys.platform))

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        "Identifies and reports edited messages"
        if before.guild.id == 850593645009698836:
            return
        channel = self.bot.get_channel(858296114415534100)
        if int(before.channel.id) == 858296114415534100 or before.author.bot == True or before.content == after.content:
            pass
        else:
            await channel.send(embed=edit_msg(before, after))

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.guild.id == 850593645009698836:
            return
        channel = self.bot.get_channel(858296114415534100)
        if int(message.channel.id) == 858296114415534100:
            pass
        else:
            await channel.send(embed=del_msg(message))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.NotOwner):
            return await ctx.send(f"{ctx.author.mention}, you are not the owner of this bot")
        return await ctx.send(str(error))

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.guild.id == 850593645009698836:
            return
        return await member.send(embed=dm_join_embed(self.bot.get_channel(852091114437738496)))

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        if member.guild.id == 850593645009698836:
            return
        channel = self.bot.get_channel(785482191592620062)
        return await channel.send(embed=leave_embed(member))

    @commands.command()
    async def invite(self, ctx):
        if ctx.author.id == 764415588873273345:
            return await ctx.author.send(os.getenv("BOT_LINK"))
        else:
            return await ctx.send("You are not authorised to use this command")


def setup(bot):
    bot.add_cog(Bot(bot))
