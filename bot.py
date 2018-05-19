import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix='!!')

@bot.event
async def on_ready():
  print("Hey look, I'm on!")
  
@bot.command()
async def say(msg):
  await bot.say(msg)
  
  
bot.run(os.environ['TOKEN'])
