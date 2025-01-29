import discord
from discord.ext import commands
import os  # If you're using an environment variable for the token

# Enable necessary intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create the bot with a command prefix
bot = commands.Bot(command_prefix="!", intents=intents)

# Event that is triggered when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    # Load the cog
    bot.load_extension("cogs.commands")

# Run the bot
bot.run(os.getenv("TOKEN"))  # Ensure your token is set in GitHub Secrets or an .env file
