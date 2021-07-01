import discord
from discord.ext import commands
import datetime


def ready_embed(platform):

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
    print(time_lag)

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
