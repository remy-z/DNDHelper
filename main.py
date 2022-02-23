import discord
import Process as p
import Recall
import PlayerInfo
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN") #get bot token stored in env file
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


@bot.command()
async def m(ctx, arg):
	print(ctx)

# roll command
@bot.command()
async def r(ctx, args):
	message = processer.rollCommand(ctx.message.content[3:])
	await ctx.channel.send(message)

@bot.command()
async def info(ctx, args):
	print(ctx.message.content)
	message = processer.info(ctx.message.content[6:])
	await ctx.channel.send(message)

@bot.command()
async def l(ctx):
	PlayerInfo
	

# shutdown bot and write data to file to reload for next time
@bot.command()
@commands.is_owner()
async def shutdown(ctx):
	# TODO WRITE OUT USER DATA TO FILE
	await ctx.bot.logout()
	print("bot is shutdown")

#executes bot
bot.run(DISCORD_TOKEN)