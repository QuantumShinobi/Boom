import logging
import discord
from discord.ext import commands
import cogs
from cogs.help import CustomHelpCommand
import sys
import os
from dotenv import load_dotenv
load_dotenv()

# Setup bot
token = os.getenv("BOT_TOKEN")
client = commands.Bot(command_prefix="b!", activity=discord.Game(
    "Listening to b!help"), intents=discord.Intents.all(), help_command=CustomHelpCommand())

for i in cogs.cogs:
    client.load_extension(f"cogs.{i}")


if sys.platform == "linux":
    from keep_repl_alive import keep_alive
    keep_alive()
    print('Waiting for bot to get ready')
    client.run(token)
else:
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
        filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
    print('Waiting for bot to get ready')
    client.run(token)
