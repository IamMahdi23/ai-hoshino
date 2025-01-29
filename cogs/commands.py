import discord
from discord.ext import commands

class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def say(self, ctx, *, message: str):
        await ctx.send(message)

    @commands.command()
    async def greet(self, ctx, name: str):
        await ctx.send(f"Hello, {name}!")

def setup(bot):
    bot.add_cog(CommandCog(bot))
