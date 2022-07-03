import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = commands.Bot(command_prefix = '!')

@client.event
async def  on_ready():
	print('Bot is live')


@client.command()
async def  ping(ctx):
	await ctx.send('Pong')

@client.command()
async def  help1(ctx):
	await ctx.send('1- Opcion 1 , 2 - Opcion 2')


client.run(TOKEN)