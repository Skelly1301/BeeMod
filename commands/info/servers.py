@bot.command(brief="Server list", description="Shows how many servers the bot is in")
async def servers(ctx):
    await ctx.send("I'm in " + str(len(bot.guilds)) + " servers!")
