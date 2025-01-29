import os
import discord
from discord.ext import commands

intents = discord.Intents.default()  # You can customize intents here.
intents.message_content = True  # Enable the message content intent (for bot commands to work).

bot = commands.Bot(command_prefix="!", intents=intents)

# Load extensions (cogs)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    # Load commands cog
    await bot.load_extension("cogs.commands")


# Run the bot
bot.run(os.getenv("TOKEN"))
