import discord, time
from discord.ext import commands
from discord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument, CommandOnCooldown, MemberNotFound, CommandInvokeError)

class OnCommandError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "hidden"

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exc):
        error = discord.Embed(colour = discord.Colour.brand_red())
        error.set_thumbnail(url='https://i.imgur.com/hXnAHqc.png')
        if isinstance(exc, CommandOnCooldown):
            if exc.retry_after <= 600:
                error.add_field(name="That command is on cooldown!", value=f"Try using this command again in {exc.retry_after:,.2f} secs.")
                await ctx.reply(embed=error)
            else:
                error.add_field(name="That command is on cooldown!", value=f"Try using this command again <t:{int(exc.retry_after + time.time())}:R>")
                await ctx.reply(embed=error)
        elif isinstance(exc, CommandNotFound):
            error.add_field(name="Invalid Command!", value="This command does not exist!")
            await ctx.reply(embed=error)
        elif isinstance(exc, commands.MissingPermissions):
            error.add_field(name="Error!", value=f"You don't have permission to use this command!")
            await ctx.reply(embed=error)
        elif isinstance(exc, MemberNotFound):
            error.add_field(name="Member not found!", value=f"Make sure the person you are trying to view is still in the server.")
            await ctx.reply(embed=error)
        elif isinstance(exc, commands.MissingRequiredArgument):
            error.add_field(name="Error!", value=f"You forgot to provide an argument, please use the correct format.")
            await ctx.reply(embed=error)
        elif isinstance(exc, CommandInvokeError):
            error.add_field(name="Error!", value=f"Make sure you're using the correct parameters for this command! ")
            await ctx.reply(embed=error)
       
        raise exc


async def setup(bot):
    await bot.add_cog(OnCommandError(bot))
