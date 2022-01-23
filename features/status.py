@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord, lol')
    activity = discord.Game(name="b!help | " + str(len(bot.guilds)) + " servers!")
    await bot.change_presence(status=discord.Status.online, activity=activity)
