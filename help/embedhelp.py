@bot.command(brief="Shows all bot commands")
async def help(ctx):
    embed=discord.Embed(title="Help", description="All of the bot commands", color=0x109319)

    embed.set_author(name="BeeMod", icon_url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")

    embed.add_field(name="ㅤ", value="ㅤ", inline=True)

    embed.add_field(name="MODERATION", value="‎‎ㅤ", inline=False)

    embed.add_field(name="b!ban", value="Bans a discord member. Type b!help ban for more info", inline=True) 
    embed.add_field(name="b!kick", value="Kicks a discord member. Type b!help kick for more info", inline=True)
    embed.add_field(name="b!unban", value="Unbans a discord member. Type b!help unban for more info", inline=True)

    embed.add_field(name="ㅤ", value="ㅤ", inline=False)

    embed.add_field(name="FUN", value="ㅤ", inline=False)

    embed.add_field(name="b!8ball", value="Ask the 8ball a question! use b!8ball <question>", inline=True)
    embed.add_field(name="b!inspire", value="Use this command and the bot will return an inspirational quote", inline=True)
    
    embed.add_field(name="ㅤ", value="ㅤ", inline=False)

    embed.add_field(name="OTHER", value="ㅤ", inline=False)

    embed.add_field(name="b!servers", value="Shows how manys servers the bot is in.",inline=True)
    embed.add_field(name="b!website", value="Shows the bots website.", inline=True)

    embed.set_footer(text="Made by Skelly b!credits")
    
    await ctx.send(embed=embed)
