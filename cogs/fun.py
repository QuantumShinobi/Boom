from discord.ext import commands
import requests
import discord
from .descriptions import joke_description, meme_description
from utils.colours import give_random_color
import random


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
        # Old api fo`r jokes https://official-joke-api.appspot.com/jokes/general/random
        # New API for jokes https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw
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

    @commands.command(aliases=['pfp'])
    async def avatar(self, ctx: commands.Context, *, member: discord.Member = None):
        if member is None:
            member = ctx.author

        embed = discord.Embed(color=give_random_color(),
                              title=f"{member.name}'s Avatar")
        embed.set_image(url=member.avatar_url)
        embed.set_footer(
            text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed=embed)

    @commands.command()
    async def insult(self, ctx: commands.Context, *, member: discord.Member = None):
        await ctx.send("Sorry, this command can no longer be used")
        # if member is None:
        #     member = ctx.author
        # insult_api = "https://insult.mattbas.org/api/insult"
        # insult = requests.get(insult_api).text
        # await ctx.send(f"{ctx.author.mention}\n{insult}")

    @commands.command()
    async def inspire(self, ctx: commands.Context):
        quote_url = "https://zenquotes.io/api/random"
        response = requests.get(quote_url)
        json = response.json()
        title = json[0]['q']
        description = json[0]['a']
        embed = discord.Embed(colour=give_random_color(),
                              title=f'"{title}"', description=f"-{description}")
        await ctx.message.reply(embed=embed)

    # @commands.command()
    # async def dog(self, ctx: commands.Context):
    #     dog_url = "https://some-random-api.ml/img/dog"
    #     fact_url = "https://some-random-api.ml/facts/dog"
    #     response = requests.get(dog_url)
    #     response2 = requests.get(fact_url)
    #     json = response.json()
    #     json2 = response2.json()

    #     fact = json2['fact']
    #     url = json['link']

    #     embed = discord.Embed(colour=give_random_color(), title="Doggo!")
    #     embed.set_image(url=url)
    #     embed.add_field(name="Fact:", value=fact)
    #     await ctx.message.reply(embed=embed)

    @commands.command(aliases=["au", "av_u"])
    async def avatar_url(self, ctx: commands.Context, *, member: discord.Member = None):
        if not member:
            member = ctx.author
        await ctx.send(f"{member.name}'s avatar url\n{member.avatar_url}")

    @commands.command()
    async def pikachu(self, ctx: commands.Context):
        pikachu_url = "https://some-random-api.ml/img/pikachu"
        response = requests.get(pikachu_url)
        json = response.json()
        url = json['link']

        embed = discord.Embed(colour=give_random_color(), title="Pika!")
        embed.set_image(url=url)
        await ctx.message.reply(embed=embed)

    @commands.command()
    async def kill(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
            die = ["died because they were watching too much TikTok",
                   "died because of too much cringe",
                   "died because they ate too much spaghetti",
                   "just randomly disappeared from the universe",
                   "thought they were cool and did a dangerous stunt which went miserably and died",
                   "died because why not",
                   f"died because {ctx.author.mention} stabbed them in the stomach",
                   "died because they messed with the cops, rip",
                   "died due to malnutrition",
                   "died because they ate too much cheeseburst pizza",
                   "died because they got shot while robbing a bank",
                   "tried to become an astronaut but died because their spaceship exploded, rip",
                   "stubbed their toe and died",
                   "cannot be killed because they are invincible ... ||sike||",
                   "was killed by aliens",
                   "was killed by the impostor"]

            await ctx.send(member.mention+" "+random.choice(die))

    @commands.command(aliases=['pm'])
    async def pokememe(self, ctx):
        meme_url = "https://meme-api.herokuapp.com/gimme/MandJTV"
        while True:
            response = requests.get(meme_url)
            json = response.json()
            ups = json['ups']
            if json['nsfw'] == False or json['nsfw'] == "false":
                embed = discord.Embed(title=json['title'],
                                      url=json['postLink'],
                                      color=give_random_color())
                embed.set_image(url=json['url'])
                embed.set_footer(text=f"👍: {ups} 👎: 0")
                await ctx.message.reply(embed=embed)
                break


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
