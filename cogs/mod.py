import discord
from discord.ext import commands
from utils.colours import give_random_color


class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

        # Kick Command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member != self.client.user and member.top_role < ctx.author.top_role:
            try:
                await member.send(f"You have been kicked from {ctx.guild.name}, because {reason}")
            except:
                await ctx.send(f"{member.mention} has their DMs closed, so I cannot send them a DM saying they are kicked")
            await member.kick(reason=reason)
            await ctx.send(f'{member.mention} was kicked.')
        elif member != self.client.user and member.top_role > ctx.author.top_role or member.top_role == ctx.author.top_role:
            await ctx.reply("This member cannot be kicked as they are equal are higher than you in the hierarchy")
        elif member == self.client.user:
            await ctx.reply("You cannot kick me using me :/")


@commands.command()
@commands.has_permissions(ban_members=True)
async def ban(self, ctx, member: discord.Member, *, reason=None):
    if member != self.client.user and member.top_role < ctx.author.top_role:
        try:
            await member.send(f"You were banned in {ctx.guild.name}, because +{reason}")
        except:
            await ctx.send("{member.mention} has their DMs closed, so I cannot send them a DM saying they are banned")
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} was banned.')

    elif member != self.client.user and member.top_role > ctx.author.top_role or member.top_role == ctx.author.top_role:
        await ctx.reply("This member cannot be banned as they are equal are higher than you in the hierarchy")
    elif member == self.client.user:
        await ctx.reply("You cannot ban me using me :/")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount + 1)

    @commands.command(aliases=['m'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedrole = discord.utils.get(guild.roles, name="Muted")

        if not mutedrole:
            mutedrole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedrole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        if mutedrole in member.roles:
            await ctx.reply(
                "They is already muted"
            )
        elif member != self.client.user and member.top_role < ctx.author.top_role:
            try:
                await member.send(f"You were muted in the server {guild.name} for reason: {reason}")
            except:
                await ctx.send(f"{member.mention} has their DMs closed, so I cannot send them a DM saying they are muted")

            await member.add_roles(mutedrole, reason=reason)
            emd = discord.Embed(
                title="Member muted!", description=f"{member.mention} has been muted \n\nReason: {reason}", color=give_random_color())
            emd.set_footer(
                text=f"Muted by {ctx.author.name}#{ctx.author.discriminator}")
            emd.set_thumbnail(url=f"{member.avatar_url}")
            await ctx.reply(embed=emd)
            # await ctx.send(f"Muted {member.mention} for reason: {reason}")

        elif member != self.client.user and member.top_role > ctx.author.top_role or member != self.client.user and member.top_role == ctx.author.top_role:
            await ctx.reply("This member cannot be muted or temporarily muted as they are equal or higher than you in the hierarchy")

        elif member == self.client.user:
            await ctx.send("You cannot mute me using me :/")


def setup(bot: commands.Bot):
    bot.add_cog(Mod(bot))
