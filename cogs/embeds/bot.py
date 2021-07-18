import discord
from discord import Color
import datetime


def ready_embed(platform):
    """
    Embed for bot's startup message
    """

    embed = discord.Embed(title="Bot has started/restarted",
                          description="Bot has started running, here are the details", color=discord.Color.blurple())
    local_timezone = datetime.datetime.now(
        datetime.timezone.utc).astimezone().tzinfo
    time = datetime.datetime.now()
    utc = datetime.datetime.utcnow()
    if utc > time:
        time_lag = utc-time
    else:
        time_lag = time-utc

    if platform == "linux":
        server = "replit"
    else:
        server = "Ash's computer"
    embed.add_field(name="Running on", value=server, inline=False)
    embed.add_field(name="Server timezone", value=local_timezone, inline=True)
    embed.add_field(name="Sever time", value=f"{time}", inline=True)
    embed.add_field(name="UTC time", value=f"{utc}", inline=True)
    embed.add_field(name="Time lag(according to UTC)",
                    value=str(time_lag), inline=False)
    return embed


def edit_msg(before, after):
    """
    Embed for edited message reporting
    """
    embed = discord.Embed(
        color=Color.blue(), url="https://github.com/IamEinstein/Boom", title=f"{before.author} edited a message", timestamp=datetime.datetime.now())
    embed.set_thumbnail(url=before.author.avatar_url)
    embed.add_field(name="Original Message",
                    value=f'{before.content}', inline=False)
    embed.add_field(name="Edited Message",
                    value=f'{after.content}', inline=True)
    embed.add_field(
        name="Channel", value=f"{before.channel.mention}", inline=True)
    return embed


def del_msg(message):
    """
    Embed for deleted message reporting
    """
    embed = discord.Embed(
        color=Color.blue(), url="https://github.com/IamEinstein/Boom", title=f"{message.author} deleted a message", timestamp=datetime.datetime.now())
    embed.set_thumbnail(url=message.author.avatar_url)

    embed.add_field(name="Message Content",
                    value=f'{message.content}', inline=False)
    embed.add_field(
        name="Channel", value=f"{message.channel.mention}", inline=True)
    return embed
