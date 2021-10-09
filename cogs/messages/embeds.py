import datetime
from mongo import PollModel
import discord
from discord import Embed, Color
from utils.tz import datetime_from_utc_to_local, format_time, IST
from discord.ext import commands
from utils.colours import give_random_color


def create_team_emded(time: int, game: str):
    embed = Embed(colour=give_random_color(
    ), description=f"Time to play {game.content},react with  👍 if u in", title="Matchmaking")
    embed.set_footer(text=f"Ends in {str(time)} seconds")

    return embed


def ready_embed(platform):
    """
    Embed for bot's startup message
    """

    embed = discord.Embed(title="Bot has started/restarted",
                          description="Bot has started running, here are the details", color=give_random_color())
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
        color=give_random_color(), url=before.jump_url, title=f"{before.author} edited a message", timestamp=datetime.datetime.now())
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
        color=give_random_color(), url=message.jump_url, title=f"{message.author} deleted a message", timestamp=datetime.datetime.now())
    embed.set_thumbnail(url=message.author.avatar_url)

    embed.add_field(name="Message Content",
                    value=f'{message.content}', inline=False)
    embed.add_field(
        name="Channel", value=f"{message.channel.mention}", inline=True)
    return embed


async def log_poll(poll: PollModel, bot: commands.Bot):
    time_started = format_time(IST.localize(
        datetime_from_utc_to_local(poll['start_time'])))
    time_ended = format_time(IST.localize(
        datetime_from_utc_to_local(poll['end_time'])))
    msg_id = poll['poll_id']
    reaction_count = poll['winner_reaction_count']
    guild = bot.get_channel(int(poll['channel_id'])).guild
    message = await bot.get_channel(int(poll['channel_id'])).fetch_message(msg_id)
    icon_url = guild.icon_url
    guild_name = guild.name
    url = message.jump_url
    embed = discord.Embed(
        title=f"Poll ended in {guild_name}", url=url, thumbnail=icon_url, color=give_random_color())
    embed.add_field(name="Poll topic", value=poll['title'])
    embed.add_field(
        name=f"Started", value=str(time_started))
    embed.add_field(name=f"Ended", value=str(time_ended))
    embed.add_field(name="Ended at",
                    value=f"{str(datetime.datetime.now(tz=IST))}")
    embed.add_field(
        name=f"Winner", value=f"Winner {poll['winner']}, Votes: {reaction_count}")
    return embed


def dm_join_embed(channel):
    embed = discord.Embed(colour=give_random_color(), title=f"Welcome to Boom",
                          description=f"Welcome to Boom. Kindly check the rules here, {channel.mention}.", timestamp=datetime.datetime.now(IST))
    return embed


def approved_embed(user):
    embed = discord.embed(color=give_random_color(), title="Registration successful",
                          description=f"Hi {user.mention}, we are glad to announce that your registration for the chronic members clan has been approved.")
    return embed


def info_embed(ctx: commands.Context, author: discord.User = None):

    user = ctx.author
    id = user.id
    avatar_url = user.avatar
    time_created = user.created_at
    embed = discord.Embed(colour=give_random_color(
    ), title="User information", timestamp=datetime.datetime.now())
    embed.add_field(name="id", value=id, inline=False)
    embed.set_thumbnail(url=avatar_url)
    embed.add_field(name="Creation Date", value=format_time(
        time_created), inline=False)
    embed.add_field(name="Username", value=f"{user.name}#{user.discriminator}")
    icon = ctx.bot.user.avatar
    embed.set_footer(text="Boom", icon_url=icon)
    return embed


def leave_embed(user: discord.User):
    embed = discord.Embed(colour=give_random_color(
    ), title="A Member has left us.", description=f"{user.mention} has left the server")
    return embed


def animal_image_embed(img_url: str, fact: str, animal):
    embed = discord.Embed(colour=give_random_color(),
                          title=f"{animal}", description=f"{fact}")
    embed.set_image(url=img_url)
    return embed
