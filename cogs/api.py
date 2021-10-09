import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv
import io
from aiohttp import ClientSession
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

    # Canvas Commands

    @commands.command()
    async def glass(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/glass?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'glass.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def wasted(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/wasted?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'wasted.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def passed(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/passed?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'passed.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def jail(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/jail?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'jail.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def comrade(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/comrade?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'comrade.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def triggered(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/triggered?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'triggered.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command(aliases=['colour'])
    async def color(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/gay?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'colour.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    # Image Manipulation commands

    @commands.command(aliases=["grey", "gray", "greyscale"])
    async def grayscale(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/greyscale?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'greyscale.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def invert(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/invert?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'invert.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command(aliases=["invert_greyscale", "i_greyscale", "invert_g", "i_grey"])
    async def invertgreyscale(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/invertgreyscale?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'invertgreyscale.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def brightness(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/brightness?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'brightness.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def threshold(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/threshold?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'threshold.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def sepia(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/sepia?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'sepia.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def red(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/red?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'red.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def green(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/green?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'green.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def bloo(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/bloo?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'bloo.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def blurple(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/blurple?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'blurple.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def blurple2(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/blurple2?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'blurple2.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")
    # TODO:COLOR COMMAND
    # @commands.command()
    # async def color(self, ctx: commands.Context, *, member: discord.Member = None, color:str=):
    #     await ctx.trigger_typing()

    #     if member is None:
    #         member = ctx.author
    #     avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
    #     async with ClientSession() as session:
    #         async with session.get(os.getenv("API")+f"/canvas/color?avatar={avatar_url}") as response:
    #             if response.status == 200:
    #                 fp = io.BytesIO(await response.read())
    #                 await ctx.reply(file=discord.File(fp, 'color.png'))
    #             else:
    #                 print(await response.read())
    #                 print(response.status)
    #                 await ctx.reply("Couldn't get image")
    @commands.command()
    async def pixelate(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/pixelate?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'pixelate.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command()
    async def blur(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()

        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/blur?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'blur.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")
    # Fakes, Fake comments, fake tweets and other "fake" stuff 😂

    @commands.command(aliases=['yt', 'comment'])
    async def youtube(self, ctx: commands.Context, member: discord.Member = None, *, comment: str):
        await ctx.trigger_typing()
        if member == None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        username = member.name
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/canvas/youtube-comment?avatar={avatar_url}&comment={comment}&username={username}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'yt.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command(aliases=['twitter'])
    async def tweet(self, ctx: commands.Context, member: discord.Member = None, *, comment: str):
        await ctx.trigger_typing()
        if member == None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        username = member.name
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"canvas/tweet?avatar={avatar_url}&comment={comment}&username={username}&displayname={username}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'tweet.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command(aliases=['it_stupid', "its_so_stupid"])
    async def stupid(self, ctx: commands.Context, member: discord.Member = None, *, dog):
        await ctx.trigger_typing()
        if member == None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        username = member.name
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"canvas/its-so-stupid?avatar={avatar_url}&dog={dog}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'stupid.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command(aliases=['simpcard', "simp_card"])
    async def simp(self, ctx: commands.Context, member: discord.Member = None):
        await ctx.trigger_typing()
        if member == None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        username = member.name
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"canvas/simpcard?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'simp.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command(aliases=["lol_police"])
    async def lolice(self, ctx: commands.Context, member: discord.Member = None):
        await ctx.trigger_typing()
        if member == None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        username = member.name
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"canvas/lolice?avatar={avatar_url}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'lolice.png'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    # Special premium Commands
    @commands.command(aliases=['pp'])
    async def petpet(self, ctx: commands.Context, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        key = os.environ.get('API_KEY')
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/premium/petpet?avatar={avatar_url}&key={key}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'petpet.gif'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")

    @commands.command(aliases=['amongus', 'among', 'among_us', 'imposter'])
    async def sus(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        avatar_url = str(member.avatar_url_as(format="png", size=1024))[0:-10]
        key = os.environ.get('API_KEY')
        async with ClientSession() as session:
            async with session.get(os.getenv("API")+f"/premium/amongus?avatar={avatar_url}&key={key}&username={member.name}") as response:
                if response.status == 200:
                    fp = io.BytesIO(await response.read())
                    await ctx.reply(file=discord.File(fp, 'among_us.gif'))
                else:
                    print(await response.read())
                    print(response.status)
                    await ctx.reply("Couldn't get image")
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
