import discord
import discord.ext.commands import Bot
import discord.ext import commands
import asyncio

bot = commands.Bot(prefix='!!')

@bot.event
async def on_ready():
  print("Hey look, I'm on!")
  
@bot.commands()
async def say(msg):
  await bot.say(msg)
  
  
bot.run(os.environ['TOKEN'])
