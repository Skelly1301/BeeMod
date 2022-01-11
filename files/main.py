import os
from keep_alive import keep_alive
from discord.ext import commands
import discord

bot = commands.Bot(
	command_prefix="s!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 23894702958  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier
    activity = discord.Game(name="test", type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)

extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("TOKEN") 
