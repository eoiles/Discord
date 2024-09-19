'''
This is  the final main.py

'''

#the token of the discord bot
import discord
from discord.ext import commands
from UI.mainmenu import MainMenu  # Adjust the import based on your structure

# Your bot's token
#token will import from token file
with open('token', 'r') as file:
    token = file.read().strip()

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	if message.content == '/main':
		main_menu = MainMenu()
		await message.channel.send("Main Menu:", view=main_menu)

	await bot.process_commands(message)  # Ensure other commands are processed

# Run the bot
bot.run(token)