from discord.ext import commands
import discord
import aiohttp
import io
import os
from dotenv import load_dotenv
from helpers.encrypt import decrypt_url
load_dotenv()
key = os.getenv("API_KEY")
petpet_tag = b'n\xe2\xba1i\xf8\xcc@\tu\x0eil3Ho'
encrypt_petpet = b'\xfb\x0e\xc1\x82\xd6\x001h\xa2+\x9d2\xd9\xb3\xa3d\x1fy\x84j\xac\xd7/4\x92lc5\xb0\xf7\xb0CB\xf1\x02I\xef\xea\xbc\x82\xae\xad'


class PikaBot(commands.Cog):
    """
    Thanks @PichuPikaRai for this code
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def lyrics(self, ctx, *, song):
        pass

    @commands.command()
    async def add(self, ctx, num1: float, num2: float):
        await ctx.send(num1 + num2)

    @commands.command()
    async def subtract(self, ctx, num1: float, num2: int):
        await ctx.send(num1 - num2)

    @commands.command()
    async def divide(self, ctx, num1: float, num2: float):
        await ctx.send(num1 / num2)

    @commands.command()
    async def multiply(self, ctx, num1: float, num2: float):
        await ctx.send(num1 * num2)

    @commands.command()
    async def petpet(self, ctx: commands.Context, *, member: discord.Member = None):
        petpet_url = decrypt_url(encrypted_url=encrypt_petpet, tag=petpet_tag)
        if member == None:
            member = ctx.author

        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            u = petpet_url[2:-2]
            async with session.get(
                    f"{u}?username={member.name}&avatar={member.avatar}&key={key}"
            ) as resp:

                if 300 > resp.status >= 200:
                    fp = io.BytesIO(await resp.read())

                    await ctx.reply(file=discord.File(fp, 'petpet.gif'))
                else:
                    await ctx.reply('Couldnt get image :(')

                await session.close()

    @commands.command()
    async def avatar(ctx, *, member: discord.Member = None):
        await ctx.send(member.avatar_url)

    # Kick Command

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.send("You have been kicked from CG | Community, because"+reason)
        await member.kick(reason=reason)
        await ctx.send(f'{member} was kicked.')

    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the permission to kick people")

    # Ban Command

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.send("You have been banned from CG | Community, because"+reason)
        await member.ban(reason=reason)
        await ctx.send(f'{member} was banned.')

    @ban.error
    async def ban_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the permission to ban people")


def setup(bot: commands.Bot):
    bot.add_cog(PikaBot(bot))
