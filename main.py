
from discord.ext import commands
import discord
from mongo import connect_mongo
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("BOT_TOKEN")
client = commands.Bot(command_prefix="b!",
                      activity=discord.Game("Developed by IamEinstein"), intents=discord.Intents.all())
collection = connect_mongo()


# @client.command()
# async def say(ctx, what):
#     user = client.get_user(int(os.getenv("MY_ID")))
#     await user.send(what)


@client.event
async def on_message(message):
    args = message.content.split()
    if "help" in args:
        await message.channel.send(f"Please type `{client.command_prefix}help` for more information")
    await client.process_commands(message)


@client.event
async def on_ready():
    channel = client.get_channel(858296114415534100)
    await channel.send(f"Bot is ready")


@client.event
async def on_message_edit(before, after):
    channel = client.get_channel(858296114415534100)
    await channel.send(f"{before.author.mention} edited a message from\n `{before.content}` to `{after.content}`")


@client.event
async def on_message_delete(message):
    channel = client.get_channel(858296114415534100)
    await channel.send(f"{message.author.mention} you deleted a message:\n  {message.content}")

client.run(token)
