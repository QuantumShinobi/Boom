from discord_slash import SlashCommand, cog_ext, SlashContext
from discord.ext.commands import Bot, Cog
from discord import Embed
import discord
import requests
from utils.colours import give_random_color


class Slash(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="test_cog_slash", guild_ids=[850593645009698836])
    async def _test_cog_slash(self, ctx: SlashContext):
        embed = Embed(title="Embed Test")
        await ctx.send(embed=embed)
    from discord_slash.utils.manage_commands import create_option

    @cog_ext.cog_slash(name="test_options",
                       description="This is just a test command, nothing more.",
                       guild_ids=[850593645009698836],
                       options=[
                           create_option(
                               name="optone",
                               description="This is the first option we have.",
                               option_type=3,
                               required=False
                           )
                       ])
    async def _test_options(ctx: SlashContext, optone: str):
        await ctx.send(content=f"I got you, you said {optone}!")

    @cog_ext.cog_slash(name="ping", guild_ids=[850593645009698836])
    async def ping(self, ctx: SlashContext):
        await ctx.send(content="Pong!")

    @cog_ext.cog_slash(name="joke", guild_ids=[850593645009698836])
    async def _joke(self, ctx: SlashContext):
        joke_url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw"
        response = requests.get(joke_url)
        json = response.json()
        print(json)
        type = json['type']
        if type == "single":
            joke = json['joke']
            category = json['category']
            embed = discord.Embed(color=give_random_color(),
                                  title="Here's a joke for ya!", description=joke)
            # embed.add_field(name="category", value=category)
            await ctx.message.reply(embed=embed)
        else:
            setup = json['setup']
            delivery = json['delivery']
            category = json['category']

            embed = discord.Embed(color=give_random_color(),
                                  title="Here's a joke for ya!")
            embed.add_field(name="Question", value=setup, inline=False)
            embed.add_field(name="Answer", value=delivery, inline=False)
            # embed.add_field(name="Category", value=category)
            await ctx.message.reply(embed=embed)


def setup(bot: Bot):
    bot.add_cog(Slash(Bot))
