import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True  # Add the privileged intent

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

bot.run(os.getenv("TOKEN"))  # Token stored in GitHub secrets
