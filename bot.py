import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


from dolar import getValueUsd
from btc import getValueBTCtoUSD

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
async def dolar(ctx):
	res = await getValueUsd()
	await ctx.send(f'Estimado, el valor del dolar informal es: {res}'.format(res))


@bot.command()
async def bitcoin(ctx):
	res = await getValueBTCtoUSD()
	await ctx.send(f'Estimado, el valor del instumento fugador es: {res} USD'.format(res))

@bot.command()
async def btc(ctx):
	res = await getValueBTCtoUSD()
	await ctx.send(f'Estimado, el valor del instumento fugador es: {res} USD'.format(res))




bot.run(TOKEN)
