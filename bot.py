import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")
API_URL = os.getenv("API_URL")

@bot.command()
async def recommend(ctx, *, mood):
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, json={"mood": mood}) as response:
            books = await response.json()
    for book in books:
        embed = discord.Embed(title=book["title"], description=book["reasoning"])
        embed.add_field(name="Author", value=book["author"])    
        await ctx.send(embed=embed)

bot.run(TOKEN)