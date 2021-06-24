
from discord.ext import commands
import discord
from mongo import connect_mongo
from dotenv import load_dotenv
import os

load_dotenv()


token = os.getenv("BOT_TOKEN")
client = commands.Bot(command_prefix="!",
                      activity=discord.Game("Im being developed"), intents=discord.Intents.all())
collection = connect_mongo()


@client.command()
async def say(ctx, what):
    user = client.get_user(int(os.getenv("MY_ID")))
    await user.send(what)


@client.event
async def on_message(message):
    args = message.content.split()
    if "help" in args:
        await message.channel.send(f"Please type `{client.command_prefix}help` for more information")
    await client.process_commands(message)


@client.event
async def on_ready():
    channel = client.get_channel(int(os.getenv("CHANNEL_ID")))
    await channel.send(f"Bot is ready")

client.run(token)
