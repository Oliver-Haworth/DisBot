import discord
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("DisBot is now online!")

    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)

    if channel is None:
        print("❌Failed CHANNEL_ID.")
        return

    print(f"✅Pinging{channel.name}...")

    while True:
        await channel.send("ping")
        await asyncio.sleep(30)
        
bot.run(DISCORD_TOKEN)
