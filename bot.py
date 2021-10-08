from plistlib import load
from discord import Client, Intents, Embed
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import os
from dotenv import load_dotenv
load_dotenv()
bot = commands.Bot(intents=Intents.default(), command_prefix="b!")
slash = SlashCommand(bot)


@slash.slash(name="test", guild_ids=[850593645009698836])
async def test(ctx: SlashContext):
    embed = Embed(title="Embed Test")
    await ctx.send(embed=embed)

bot.load_extension("slash_cogs.commands")
bot.run(os.getenv("BOT_TOKEN"))
