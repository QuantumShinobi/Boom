from keep_alive import keep_alive
from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
from discord.ext.commands import has_permissions
load_dotenv()
token = os.getenv("BOT_TOKEN")
client = commands.Bot(command_prefix="b!",
                      activity=discord.Game("Developed by IamEinstein(Rishit)"), intents=discord.Intents.all())



# @client.command()
# async def say(ctx, what):
#     user = client.get_user(int(os.getenv("MY_ID")))
#     await user.send(what)

# @client.command(pass_context=True)
# @has_permissions(administrator=True)
# async def disable_log(ctx):
#   await client.send_message("Okay, stopping del msgs")



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
    await channel.send(f"{before.author} edited a message from\n `{before.content}` to `{after.content}` in {before.channel.mention}")


@client.event
async def on_message_delete(message):
    channel = client.get_channel(858296114415534100)
    await channel.send(f"{message.author}  deleted a message in {message.channel.mention}:\n  {message.content}")
keep_alive()
client.run(token)
