# commands.py (inside the cogs folder)

from discord.ext import commands

@commands.command()
async def ping(ctx):
    print("Ping command triggered!")
    await ctx.send("Pong!")
