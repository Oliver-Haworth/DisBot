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

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

# It will executes the bot with the specified token.
bot.run("MTQyMTA2MjM0OTAwMzE2MTY1Mw.GBtiPJ.2L4gfpn99SevLvU3s3yQOrg5psSq9oDzt84ooQ")