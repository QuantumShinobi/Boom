from discord.ext import commands
import requests
import discord
from .descriptions import joke_description, meme_description
from utils.colours import give_random_color


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description=meme_description)
    async def meme(self, ctx: commands.Context):
        meme_url = "https://meme-api.herokuapp.com/gimme"
        response = requests.get(meme_url)
        print(response.json()['url'])
        print(response.status_code)
        json = response.json()
        if json['nsfw'] == False or json['nsfw'] == "false":
            embed = discord.Embed(title=json['title'], url=json['postLink'])
            embed.set_image(url=json['url'])
            await ctx.message.reply(embed=embed)

    @commands.command(description=joke_description)
    async def joke(self, ctx: commands.Context):
        joke_url = "https://official-joke-api.appspot.com/jokes/general/random"
        response = requests.get(joke_url)
        json = response.json()
        title = json[0]['setup']
        description = json[0]['punchline']
        embed = discord.Embed(color=give_random_color(),
                              title=title, description=description)
        await ctx.message.reply(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
