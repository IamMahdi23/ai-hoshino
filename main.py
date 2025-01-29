import os
import discord
from discord.ext import commands

# Set up the bot with the command prefix
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Event triggered when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    # Load the cog that contains the commands (including !ping)
    bot.load_extension("cogs.commands")

# Run the bot with the token from environment variables (GitHub Secrets)
bot.run(os.getenv("TOKEN"))
