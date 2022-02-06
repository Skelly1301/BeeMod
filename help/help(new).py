@bot.command()
async def help(ctx):
    page1 = discord.Embed (
        title = 'BeeMod Help',
        description = 'Welcome to the BeeMod help page!\n\nNavigate between pages using the buttons below\n\nJoin the support server\nhttps://discord.gg/SUVejVrUCn',
        colour = discord.Colour.green()
    )
    page1.set_author(name="Help", icon_url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")
    page1.set_thumbnail(url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")

    page2 = discord.Embed (
        title = 'Moderation 🔨',
        description = 'All of BeeMods moderation commands',
        colour = discord.Colour.green()
    )
    page2.set_author(name="Help", icon_url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")
    page2.set_thumbnail(url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")
    page2.add_field(name="b!kick", value="Kicks a discord member. Use b!kick <user> [reason]")
    page2.add_field(name="b!ban", value="Bans a discord member. Use b!ban <user> [reason]")
    page2.add_field(name="b!unban", value="Unbans a discord member. Use b!unban <user>")
    page2.add_field(name="b!clear", value="Clears a certain number of discord messages. Use b!clear <number_of_messages>")

    page3 = discord.Embed (
        title = 'Fun 😊',
        description = 'All of BeeMods fun commands',
        colour = discord.Colour.green()
    )
    page3.set_author(name="Help", icon_url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")
    page3.set_thumbnail(url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")
    page3.add_field(name="b!8ball", value="Ask the magic 8ball a question! Use b!8ball <question>")
    page3.add_field(name="b!meme", value="Sends a random meme from r/memes")
    page3.add_field(name="b!rps", value="Play rock paper scissors with BeeMod! Use b!rps <item>")
    page3.add_field(name="b!inspire", value="Sends a random, inspirational quote")

    page4 = discord.Embed (
        title = 'Utilities 🎉',
        description = 'All of BeeMods utility commands',
        colour = discord.Colour.green()
    )
    page4.set_author(name="Help", icon_url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")
    page4.set_thumbnail(url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")
    page4.add_field(name="b!gstart", value="Starts a giveaway! Use b!gstart <how_many_minutes_you_want_it_to_last> [prize]")
    page4.add_field(name="b!lvl", value="See your server level! To see another user's level use b!lvl @user")
    page4.add_field(name="b!servers", value="See how many servers the bot is in")
    page4.add_field(name="b!website", value="Shows the bot's website")

    page5 = discord.Embed (
        title = 'Economy 💸',
        description = 'All of BeeMods economy commands',
        colour = discord.Colour.green()
    )
    page5.set_author(name="Help", icon_url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")
    page5.set_thumbnail(url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")
    page5.add_field(name="b!bal", value="Check your wallet & bank balance")
    page5.add_field(name="b!beg", value="Beg for some coins")
    
    pages = [page1, page2, page3, page4, page5]

    message = await ctx.send(embed = page1)
    await message.add_reaction('◀')
    await message.add_reaction('▶')

    def check(reaction, user):
        return user == ctx.author

    i = 0
    reaction = None

    while True:
        if str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '▶':
            if i < 4:
                i += 1
                await message.edit(embed = pages[i])
        
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 300.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()
