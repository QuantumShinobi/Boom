from datetime import datetime
import discord
from discord.ext import commands
from utils.colours import give_random_color
from utils.tz import IST


class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__(command_attrs={
            "help": "Show help about the bot, a command, or a category."})

    async def on_help_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(str(error.original))

    @staticmethod
    def make_page_embed(commands, title="Boom Help", description=discord.Embed.Empty):
        embed = discord.Embed(
            color=0xFE9AC9, title=title, description=description)
        embed.set_footer(
            text=f'Use "b!help command" for more info on a command.'
        )

    @staticmethod
    def make_default_embed(cogs, title="Categories", description=discord.Embed.Empty):
        embed = discord.Embed(
            color=0xFE9AC9, title=title, description=description)
        counter = 0
        for cog in cogs:
            cog = cog
            description = cog.description
            description = f"{description or 'No Description'} \n {''.join([f'`{command.qualified_name}` ' for command in cog.commands])}"
            embed.add_field(name=cog.qualified_name,
                            value=description, inline=False)
            counter += 1

        return embed

    async def send_bot_help(self, mapping):
        embed = discord.Embed(color=give_random_color(),
                              title="Boom Help", description="Below is the list of commands. Pls type b!help <command> to get more information.", timestamp=datetime.now(tz=IST))
        embed.set_footer(text=":)", icon_url=discord.Embed.Empty)
        commands = mapping.values()
        # Arrange according to category
        # 1. Get all keys as list
        # 2. Iterate through list to get values
        # 3.Add the values in that category
        for command_list in commands:

            for command in command_list:
                if command.description != None and command.description != "" and command.name != "help" and command.name != "invite":
                    embed.add_field(name=f"{command.name}",
                                    value=f"{command.description}", inline=False)
                elif command.name != "help" and command.name != "invite":
                    embed.add_field(name=f"{command.name}",
                                    value=f"No description", inline=True)

        await self.context.message.reply(embed=embed)

    async def send_cog_help(self, cog):
        ctx = self.context
        ctx.invoked_with = "help"
        bot = ctx.bot
        commands = bot.commands

        filtered = await self.filter_commands(cog.get_commands(), sort=True)

        embed = self.make_page_embed(
            filtered,
            title=(cog and cog.qualified_name or "Other") + " Commands",
            description=discord.Embed.Empty if cog is None else cog.description,
        )

        await ctx.send(embed=embed)

    async def send_group_help(self, group):
        ctx = self.context
        ctx.invoked_with = "help"
        bot = ctx.bot

        subcommands = group.commands
        if len(subcommands) == 0:
            return await self.send_command_help(group)

        filtered = await self.filter_commands(subcommands, sort=True)

        embed = self.make_page_embed(
            filtered,
            title=group.qualified_name,
            description=f"{group.description}\n\n{group.help}"
            if group.description
            else group.help or "No help found...",
        )

        await ctx.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(
            color=0xFE9AC9, title=f"cg!{command.qualified_name}"
        )

        if command.description:
            embed.description = f"{command.description}\n\n{command.help}"
        else:
            embed.description = command.help or "No help found..."

        embed.add_field(name="Signature",
                        value=self.get_command_signature(command))

        await self.context.send(embed=embed)


def setup(bot):
    bot.old_help_command = bot.help_command
    bot.help_command = CustomHelpCommand()


def teardown(bot):
    bot.help_command = bot.old_help_command
