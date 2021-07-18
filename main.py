import logging
import discord
from discord.ext import commands
from cogs.bot import Bot
from cogs.commands import RMTCommands
from cogs.poll import Poll
import sys
import os
from dotenv import load_dotenv
load_dotenv()
# Setup logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# Setup bot
token = os.getenv("BOT_TOKEN")
client = commands.Bot(command_prefix="b!",
                      activity=discord.Game("Developed by Ash"), intents=discord.Intents.all(), help_command=None)
client.add_cog(Bot(client))
client.add_cog(RMTCommands(client))
client.add_cog(Poll(client))
if sys.platform == "linux":
    from keep_alive import keep_alive
    keep_alive()
    print('Waiting for bot to get ready')
    client.run(token)
else:
    print('Waiting for bot to get ready')
    client.run(token)
