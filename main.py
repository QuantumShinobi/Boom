import discord
from discord.ext import commands
from cogs.bot import Bot
from cogs.commands import RMTCommands
from cogs.poll import Poll
import sys
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("BOT_TOKEN")
client = commands.Bot(command_prefix="b!",
                      activity=discord.Game("Developed by IamEinstein(Rishit)"), intents=discord.Intents.all(), help_command=None)
client.add_cog(Bot(client))
client.add_cog(RMTCommands(client))
if sys.platform == "linux":
    from keep_alive import keep_alive
    keep_alive()
    client.run(token)
else:
    client.add_cog(Poll(client))
    client.run(token)
