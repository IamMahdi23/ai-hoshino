from discord.ext import commands

# Define the ping command inside the cog
@commands.command()
async def ping(ctx):
    await ctx.send("Pong!")

