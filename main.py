import discord
import Process as p
import Recall
import PlayerInfo
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!") #client object from discord.py

processer = p.Process() #class for processing messages
# event listener for when bot is switched online.
@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count += 1
	print("DND Helper is in " + str(guild_count) + " server.")

# event listener for new messages
@bot.event
async def on_message(message):
	if message.content[0] == "/":
		sendThis = processer.process(message)
		await message.channel.send(sendThis)
	await bot.process_commands(message)

# shutdown bot and write data to file to reload for next time
@bot.command()
async def m(ctx, arg):
	print(ctx)

# roller
@bot.command()
async def r(ctx, args):
	message = processer.roll(ctx.message.content[3:])
	await ctx.channel.send(message)

@bot.command()
async def info(ctx, args):
	print(ctx.message.content)
	message = processer.info(ctx.message.content[6:])
	await ctx.channel.send(message)

@bot.command()
async def l(ctx):
	#TODO DO WHATEVER THE LAST USERS COMMAND DID 
	await ctx.channel.send("yoyoyo")

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
	# TODO WRITE OUT USER DATA
	await ctx.bot.logout()
	print("bot is shutdown")

#executes bot
bot.run(DISCORD_TOKEN)