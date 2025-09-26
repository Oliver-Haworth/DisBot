# Import the os module.
import os
# Import the discord module.
import discord
from discord.ext import commands
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
# Loads the .env file that lies on the same level as the main.py.
load_dotenv()
# Grab the token as string from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

# It will executes the bot with the specified token.
bot.run(DISCORD_TOKEN)