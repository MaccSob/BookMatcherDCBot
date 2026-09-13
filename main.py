import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")

@bot.command()
async def recommend(ctx, *, mood):
    await ctx.send(f"pretending to recommend books for mood: {mood}")

bot.run(TOKEN)