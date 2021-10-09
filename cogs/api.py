import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv
from utils.colours import give_random_color
from .messages.embeds import animal_image_embed
load_dotenv()
apis = {
    "lyrics": f"{os.getenv('API')}/lyrics?",
    "dictionary": "",
    "covid": "",
    "ig": "",
    "weather": "https://rapidapi.com/foreca-ltd-foreca-ltd-default/api/foreca-weather/",
    "amazon": "",
    "movies": "",
    "telegram": "",
    "news": "",
    "website screenshots": "",
    "cricket": "",
    "ipl": "",
    "food": "",
    "translation": "",
}


class API(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Commands for animal images
    @commands.command(aliases=['Dog'])
    async def dog(self, ctx: commands.Context):
        url = os.getenv("API")+"/animal/dog"
        json = requests.get(url).json()
        await ctx.reply(embed=animal_image_embed(img_url=json['image'], fact=json['fact'], animal="Dog"))

    @commands.command()
    async def cat(self, ctx: commands.Context):
        url = os.getenv("API")+"/animal/cat"
        json = requests.get(url).json()
        await ctx.reply(embed=animal_image_embed(img_url=json['image'], fact=json['fact'], animal="Cat"))

    @commands.command()
    async def panda(self, ctx: commands.Context):
        url = os.getenv("API")+"/animal/panda"
        json = requests.get(url).json()
        await ctx.reply(embed=animal_image_embed(img_url=json['image'], fact=json['fact'], animal="Panda"))

    @commands.command()
    async def fox(self, ctx: commands.Context):
        url = os.getenv("API")+"/animal/fox"
        json = requests.get(url).json()
        await ctx.reply(embed=animal_image_embed(img_url=json['image'], fact=json['fact'], animal="Fox"))

    @commands.command(aliases=['rp', 'redpanda'])
    async def red_panda(self, ctx: commands.Context):
        url = os.getenv("API")+"/animal/red_panda"
        json = requests.get(url).json()
        img = json['image']
        await ctx.reply(embed=animal_image_embed(img_url=json['image'], fact=json['fact'], animal="Red Panda"))

    @commands.command()
    async def koala(self, ctx: commands.Context):
        url = os.getenv("API")+"/animal/koala"
        json = requests.get(url).json()
        img = json['image']
        await ctx.reply(embed=animal_image_embed(img_url=json['image'], fact=json['fact'], animal="Koala"))

    @commands.command()
    async def bird(self, ctx: commands.Context):
        url = os.getenv("API")+"/animal/bird"
        json = requests.get(url).json()
        await ctx.reply(embed=animal_image_embed(img_url=json['image'], fact=json['fact'], animal="Bird"))

    @commands.command()
    async def raccoon(self, ctx: commands.Context):
        url = os.getenv("API")+"/animal/raccoon"
        json = requests.get(url).json()
        await ctx.reply(embed=animal_image_embed(img_url=json['image'], fact=json['fact'], animal="Raccoon"))

    @commands.command()
    async def kangaroo(self, ctx: commands.Context):
        url = os.getenv("API")+"/animal/kangaroo"
        json = requests.get(url).json()
        await ctx.reply(embed=animal_image_embed(img_url=json['image'], fact=json['fact'], animal="Kangaroo"))

    # Pokedex

    @commands.command()
    async def pokedex(self, ctx: commands.Context, *, pokemon):
        url = os.getenv('API')+f"/pokedex?pokemon={pokemon}"
        json = requests.get(url).json()
        print(json)
        name = json['name']
        type = json['type'][0]
        abilities = json['abilities']
        height = json['height']
        weight = json['weight']
        base_experience = json['base_experience']
        gender = json['gender'][0]
        stats = json['stats']
        gif = json['sprites']['animated']
        description = json['description']
        generation = json['generation']
        embed = discord.Embed(title=name.capitalize(), description=description)
        embed.set_thumbnail(url=gif)
        embed.add_field(name="Type", value=type, inline=True)
        embed.add_field(name="Generation", value=type, inline=True)
        embed.add_field(name="Height", value=height, inline=True)
        embed.add_field(name="Weight", value=weight, inline=True)
        embed.add_field(name="Abilities", value=abilities, inline=True)
        embed.add_field(name="Gender", value=gender, inline=True)
        embed.add_field(name="Base Experience",
                        value=base_experience, inline=False)
        await ctx.reply(embed=embed)
        # TODO: https://pokeapi.co/docs/v2 | Pokemon evolutions, berries, games, matches and other implementations of pokeapi.com
        # stats = {"hp","attack", "defense", "sp_atk", "sp_def", "speed", "total"}

    # Anime commands

    # @commands.command()
    # async def lyrics(self, ctx, *, song):
    #     lyrics_url = apis['lyrics']+f"title={song}"
    #     await ctx.trigger_typing()
    #     response = requests.get(lyrics_url)
    #     json = response.json()

    #     title = json['title']
    #     author = json['author']
    #     lyrics = json['lyrics']

    #     if len(lyrics) <= 1501:

    #         em = discord.Embed(colour=give_random_color(),
    #                            title=title, description=lyrics)
    #         em.add_field(name="Author: ", value=author)
    #         await ctx.message.reply(embed=em)

    #     else:
    #         str = ' '
    #         em = discord.Embed(colour=give_random_color(
    #         ), title=title, description=lyrics[0: lyrics.rfind(str, 0, len(lyrics))])
    #         em.add_field(name="Author: ", value=author)
    #         await ctx.message.reply(embed=em)
    #         em = discord.Embed(colour=give_random_color(
    #         ), title=title, description=lyrics[lyrics.rfind(str, 0, len(lyrics))+1:])
    #         em.add_field(name="Author: ", value=author)
    #         await ctx.message.reply(embed=em)

    # @commands.command()
    # async def location(self, ctx: commands.Context, *, city):
    #     url = "https://foreca-weather.p.rapidapi.com/location/search/Chennai"

    #     querystring = {"lang": "en", "country": "in"}

    #     headers = {
    #         'x-rapidapi-host': "foreca-weather.p.rapidapi.com",
    #         'x-rapidapi-key': os.getenv("RAPID_API_KEY"),
    #     }
    #     response = requests.request(
    #         "GET", url, headers=headers, params=querystring)
    #     print(response.text)


def setup(bot: commands.Bot):
    bot.add_cog(API(bot))
