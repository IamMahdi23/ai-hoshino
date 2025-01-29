from discord.ext import commands

# Create a new command
@commands.command()
async def ping(ctx):
    await ctx.send("Pong!")

def setup(bot):
    bot.add_cog(CommandCog(bot))
