import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


from dolar import getValueUsd

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix = '!')

@bot.event
async def  on_ready():
	print('Bot is live :)')


@bot.command()
async def  ping(ctx):
	await ctx.send('Pong')

@bot.command()
async def dolar(ctx, arg):
	res = await getValueUsd()
	await ctx.send(f'Estimado el valor del dolar informal es: {res}'.format(res))
	
	
    


@bot.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))




bot.run(TOKEN)
