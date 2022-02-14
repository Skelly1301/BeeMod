import os
from keep_alive import keep_alive
from discord.ext import commands
import discord
from dotenv import load_dotenv
import random
import requests
import json
from requests import get
import buttons
import datetime
import asyncio
import sys
import traceback
from flask import Flask

load_dotenv()
TOKEN = os.getenv('TOKEN')
client = discord.Client()

bot = commands.Bot(command_prefix='b!', intents=discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord, lol')
    activity = discord.Activity(type=discord.ActivityType.watching,
                                name=str(len(bot.guilds)) + " servers! " +
                                " | b!help ")
    await bot.change_presence(status=discord.Status.online, activity=activity)


#moderation


@bot.command(brief="Bans a server member",
             description="b!ban <member> [reason]")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.reply(f'User {member} has been banned.')
    except:
        await ctx.reply(
            "The bot has missing permissions\n\nMake sure the Bot's top-most role is above the member's top-most role (the member who you are going to ban)"
        )


@bot.command(brief="Unbans a server member", description="b!unban <member>")
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name,
                                               member_discriminator):
            await ctx.guild.unban(user)
            await ctx.reply(f'Unbanned {user.mention}')
            return


@bot.command(brief="Kicks a server member",
             description="b!kick <member> [reason]")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.reply(f'User {member} has been kicked.')
    except:
        await ctx.reply(
            "The bot has missing permissions\n\nMake sure the Bot's top-most role is above the member's top-most role (the member who you are going to kick)"
        )


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("You don't have the permissions to do that")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You can't do that")
    else:
        print('Ignoring exception in command {}:'.format(ctx.command),
              file=sys.stderr)
        traceback.print_exception(type(error),
                                  error,
                                  error.__traceback__,
                                  file=sys.stderr)
    if isinstance(error, commands.CommandOnCooldown):
        msg = "Woah! Slow down! You have to wait {:.2f} seconds before you can do that again".format(
            error.retry_after)
        await ctx.reply(msg)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    authors = {}
    async for message in ctx.channel.history(limit=amount + 1):
        if message.author not in authors:
            authors[message.author] = 1
        else:
            authors[message.author] += 1
        await message.delete()

    msg = "\n".join([
        f"cleared {amount} messages sent by {author}"
        for author, amount in authors.items()
    ])
    await ctx.channel.send(msg, delete_after=7)


#fun


@bot.command(aliases=['8ball', '8b'])
async def _8ball(ctx):
    responses = [
        'Hell no.', 'Probably not.', 'Idk bro.', 'Probably.',
        'Hell yeah my dude.', 'It is certain.', 'It is decidedly so.',
        'Without a Doubt.', 'Yes - Definitely.', 'You may rely on it.',
        'As i see it, Yes.', 'Most Likely.', 'Outlook Good.', 'Yes!', 'No!',
        'Signs a point to Yes!', 'Reply Hazy, Try again.',
        'IDK but I do know that you should click this link https://skellyy.repl.co',
        'Better not tell you know.', 'Cannot predict now.',
        'Concentrate and ask again.', "Don't Count on it.", 'My reply is No.',
        'My sources say No.', 'Outlook not so good.', 'Very Doubtful'
    ]
    await ctx.reply(f'{random.choice(responses)}')


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    json_data[0]['a']
    return (quote)


@bot.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.reply(quote)


@bot.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content, )
    meme = discord.Embed(
        title=f"{data['title']}",
        Color=discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)


@bot.command()
async def rps(ctx, message):
    answer = message.lower()
    choices = ["rock", "paper", "scissors"]
    computers_answer = random.choice(choices)
    if answer not in choices:
        await ctx.reply(
            "That is not a valid option. Please use rock, paper or scissors")
        return
    else:
        if computers_answer == answer:
            await ctx.reply(f"Tie! We both picked {answer}")
        if computers_answer == "rock":
            if answer == "paper":
                await ctx.reply(
                    f"You win! I picked {computers_answer} and you picked {answer}!"
                )
        if computers_answer == "paper":
            if answer == "rock":
                await ctx.reply(
                    f"I win! I picked {computers_answer} and you picked {answer}!"
                )
        if computers_answer == "scissors":
            if answer == "rock":
                await ctx.reply(
                    f"You win! I picked {computers_answer} and you picked {answer}!"
                )
        if computers_answer == "rock":
            if answer == "scissors":
                await ctx.reply(
                    f"I win! I picked {computers_answer} and you picked {answer}!"
                )
        if computers_answer == "paper":
            if answer == "scissors":
                await ctx.reply(
                    f"You win! I picked {computers_answer} and you picked {answer}!"
                )
        if computers_answer == "scissors":
            if answer == "paper":
                await ctx.reply(
                    f"I win! I picked {computers_answer} and you picked {answer}!"
                )


#oldhelp


@bot.command(brief="Shows all bot commands")
async def oldhelp(ctx):
    embed = discord.Embed(title="Help",
                          description="All of the bot commands",
                          color=0x109319)

    embed.set_author(
        name="BeeMod",
        icon_url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )

    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )

    embed.add_field(name="ㅤ", value="ㅤ", inline=True)

    embed.add_field(name="MODERATION", value="‎‎ㅤ", inline=False)

    embed.add_field(
        name="b!ban",
        value="Bans a discord member. Type b!help ban for more info",
        inline=True)
    embed.add_field(
        name="b!kick",
        value="Kicks a discord member. Type b!help kick for more info",
        inline=True)
    embed.add_field(
        name="b!unban",
        value="Unbans a discord member. Type b!help unban for more info",
        inline=True)

    embed.add_field(name="ㅤ", value="ㅤ", inline=False)

    embed.add_field(name="FUN", value="ㅤ", inline=False)

    embed.add_field(name="b!8ball",
                    value="Ask the 8ball a question! use b!8ball <question>",
                    inline=True)
    embed.add_field(
        name="b!inspire",
        value="Use this command and the bot will return an inspirational quote",
        inline=True)
    embed.add_field(name="b!meme",
                    value="Reddit memes in discord",
                    inline=True)
    embed.add_field(
        name="b!rps",
        value="Use b!rps <choice> and see who wins, you or BeeMod!",
        inline=True)

    embed.add_field(name="ㅤ", value="ㅤ", inline=False)

    embed.add_field(name="UTILITIES", value="ㅤ", inline=False)

    embed.add_field(
        name="b!gstart",
        value=
        "Start a giveaway! Use !gstart <how many minutes you want it to last> <prize>",
        inline=True)
    embed.add_field(name="b!lvl", value="See your server level!", inline=True)

    embed.add_field(name="ㅤ", value="ㅤ", inline=False)

    embed.add_field(name="OTHER", value="ㅤ", inline=False)

    embed.add_field(name="b!servers",
                    value="Shows how manys servers the bot is in.",
                    inline=True)
    embed.add_field(name="b!website",
                    value="Shows the bots website.",
                    inline=True)

    embed.set_footer(text="Made by Skelly b!credits")

    await ctx.reply(embed=embed)


@bot.command()
async def help(ctx):
    page1 = discord.Embed(
        title='BeeMod Help',
        description=
        'Welcome to the BeeMod help page!\n\nNavigate between pages using the buttons below\n\nJoin the support server\nhttps://discord.gg/SUVejVrUCn',
        colour=discord.Colour.green())
    page1.set_author(
        name="Help",
        icon_url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )
    page1.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )

    page2 = discord.Embed(title='Moderation 🔨',
                          description='All of BeeMods moderation commands',
                          colour=discord.Colour.green())
    page2.set_author(
        name="Help",
        icon_url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )
    page2.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )
    page2.add_field(name="b!kick",
                    value="Kicks a discord member. Use b!kick <user> [reason]")
    page2.add_field(name="b!ban",
                    value="Bans a discord member. Use b!ban <user> [reason]")
    page2.add_field(name="b!unban",
                    value="Unbans a discord member. Use b!unban <user>")
    page2.add_field(
        name="b!clear",
        value=
        "Clears a certain number of discord messages. Use b!clear <number_of_messages>"
    )

    page3 = discord.Embed(title='Fun 😊',
                          description='All of BeeMods fun commands',
                          colour=discord.Colour.green())
    page3.set_author(
        name="Help",
        icon_url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )
    page3.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )
    page3.add_field(
        name="b!8ball",
        value="Ask the magic 8ball a question! Use b!8ball <question>")
    page3.add_field(name="b!meme", value="Sends a random meme from r/memes")
    page3.add_field(
        name="b!rps",
        value="Play rock paper scissors with BeeMod! Use b!rps <item>")
    page3.add_field(name="b!inspire",
                    value="Sends a random, inspirational quote")

    page4 = discord.Embed(title='Utilities 🎉',
                          description='All of BeeMods utility commands',
                          colour=discord.Colour.green())
    page4.set_author(
        name="Help",
        icon_url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )
    page4.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )
    page4.add_field(
        name="b!gstart",
        value=
        "Starts a giveaway! Use b!gstart <how_many_minutes_you_want_it_to_last> [prize]"
    )
    page4.add_field(
        name="b!lvl",
        value=
        "See your server level! To see another user's level use b!lvl @user")
    page4.add_field(name="b!servers",
                    value="See how many servers the bot is in")
    page4.add_field(name="b!website", value="Shows the bot's website")
    page4.add_field(name="b!news", value="View the latest BeeMod updates")

    page5 = discord.Embed(title='Economy 💸',
                          description='All of BeeMods economy commands',
                          colour=discord.Colour.green())
    page5.set_author(
        name="Help",
        icon_url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )
    page5.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )
    page5.add_field(name="b!bal", value="Check your wallet & bank balance")
    page5.add_field(name="b!beg", value="Beg for some coins")
    page5.add_field(
        name="b!dep",
        value=
        "Deposit a ceratin amount of coins into your bank. Use b!dep <amount>")
    page5.add_field(
        name="b!withdraw",
        value=
        "Withdraw a ceratin amount of coins from your bank. Use b!withdraw <amount>"
    )
    page5.add_field(
        name="b!slots",
        value="Gamble for some extra coins!. Use b!slots <amount>.")
    page5.add_field(name="b!shop", value="View the shop!")
    page5.add_field(name="b!buy",
                    value="Buy an item from the shop! Use b!buy <item>")
    page5.add_field(name="b!bag",
                    value="View the items you have bought form the shop")
    page5.add_field(
        name="b!send",
        value="Send another person some coins! Use b!send @user <amount>")
    page5.add_field(name="b!lb", value="View the BeeMod global leaderboard!")

    pages = [page1, page2, page3, page4, page5]

    message = await ctx.send(embed=page1)
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
                await message.edit(embed=pages[i])
        elif str(reaction) == '▶':
            if i < 4:
                i += 1
                await message.edit(embed=pages[i])

        try:
            reaction, user = await bot.wait_for('reaction_add',
                                                timeout=300.0,
                                                check=check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()


#other


@bot.command(brief="Bot website")
async def website(ctx):
    await ctx.reply("https://beemod.repl.co")


@bot.command(brief="Server list",
             description="Shows how many servers the bot is in")
async def servers(ctx):
    await ctx.reply("I'm in " + str(len(bot.guilds)) + " servers!")


@bot.command()
async def members(ctx):
    await ctx.reply("There are " + str(len(ctx.guild.members)) +
                    " in this server!")


#giveaway


@bot.command()
@commands.has_permissions(manage_messages=True)
async def gstart(ctx, mins: int, *, prize: str):
    embed = discord.Embed(title="Giveaway Time! 🎉",
                          description=f"{prize}",
                          color=ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds=mins * 60)

    embed.add_field(name="Ends at:", value=f"{end} UTC")
    embed.set_footer(text=f"Ends in {mins}")

    my_msg = await ctx.reply(embed=embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(mins * 60)

    new_msg = await ctx.channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}")


@bot.command()
async def news(ctx):
    em = discord.Embed(title="BeeMod Updates & News",
                       description="All the latest updates and news on BeeMod")

    em.set_author(
        name="BeeMod v1.1",
        icon_url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )

    em.add_field(name="Added b!lb command", value="v1.0.9", inline=False)
    em.add_field(
        name=
        "Finished BeeMods economy system! (First part) second part coming soon!",
        value="v1.1",
        inline=False)

    await ctx.reply(embed=em)


#leveling


@bot.event
async def on_message(message):
    if not message.author.bot:
        print('function load')
        with open('level.json', 'r') as f:
            users = json.load(f)
            print('file load')
        await update_data(users, message.author, message.guild)
        await add_experience(users, message.author, 4, message.guild)
        await level_up(users, message.author, message.channel, message.guild)

        with open('level.json', 'w') as f:
            json.dump(users, f)
    await bot.process_commands(message)


async def update_data(users, user, server):
    if not str(server.id) in users:
        users[str(server.id)] = {}
        if not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1
    elif not str(user.id) in users[str(server.id)]:
        users[str(server.id)][str(user.id)] = {}
        users[str(server.id)][str(user.id)]['experience'] = 0
        users[str(server.id)][str(user.id)]['level'] = 1


async def add_experience(users, user, exp, server):
    users[str(user.guild.id)][str(user.id)]['experience'] += exp


async def level_up(users, user, channel, server):
    experience = users[str(user.guild.id)][str(user.id)]['experience']
    lvl_start = users[str(user.guild.id)][str(user.id)]['level']
    lvl_end = int(experience**(1 / 4))
    if str(user.guild.id) != '757383943116030074':
        if lvl_start < lvl_end:
            await channel.send('{} has reached level **{}**. GG!'.format(
                user.mention, lvl_end))
            users[str(user.guild.id)][str(user.id)]['level'] = lvl_end


@bot.command(aliases=['rank', 'lvl'])
async def level(ctx, member: discord.Member = None):

    if not member:
        user = ctx.message.author
        with open('level.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(user.id)]['level']
        exp = users[str(ctx.guild.id)][str(user.id)]['experience']

        embed = discord.Embed(title='Level {}'.format(lvl),
                              description=f"{exp} XP ",
                              color=discord.Color.green())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        with open('level.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(member.id)]['level']
        exp = users[str(ctx.guild.id)][str(member.id)]['experience']
        embed = discord.Embed(title='Level {}'.format(lvl),
                              description=f"{exp} XP",
                              color=discord.Color.green())
        embed.set_author(name=member, icon_url=member.avatar_url)

        await ctx.send(embed=embed)


#economy

mainshop = [{
    "name": "Pencil",
    "price": 20,
    "description": "Write/Draw something"
}, {
    "name": "Watch",
    "price": 500,
    "description": "Check the time"
}, {
    "name": "iPhone",
    "price": 1000,
    "description": "Call people and use apps"
}, {
    "name": "iPad",
    "price": 2000,
    "description": "Use apps"
}, {
    "name": "Laptop",
    "price": 3000,
    "description": "Do work and play games"
}, {
    "name": "GamingPC",
    "price": 5000,
    "description": "Stream to Twitch and play games"
}, {
    "name": "BeeModCrown",
    "price": 1000000000,
    "description": "The ultimate item"
}]


async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["Wallet"] = 0
        users[str(user.id)]["Bank"] = 0

    with open("bank.json", 'w') as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open("bank.json", 'r') as f:
        users = json.load(f)
    return users


@bot.command(aliases=['bal'])
async def balance(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["Wallet"]
    bank_amt = users[str(user.id)]["Bank"]

    em = discord.Embed(title=f"{ctx.author.name}'s balance.",
                       color=discord.Color.teal())
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name="Bank Balance", value=bank_amt)
    await ctx.reply(embed=em)


@bot.command()
async def withdraw(ctx, amount=None):
    await open_account(ctx.author)

    if amount == None:
        em = discord.Embed(title="Please enter an amount",
                           color=discord.Color.teal())
        await ctx.reply(embed=em)
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[1]:
        em = discord.Embed(title="You don't have that much money!",
                           color=discord.Color.teal())
        await ctx.reply(embed=em)
        return
    if amount < 0:
        em = discord.Embed(title="Amount must be positive!",
                           color=discord.Color.teal())
        await ctx.reply(embed=em)
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1 * amount, "Bank")

    withdrawem = discord.Embed(title=f"You withdrew {amount} coins!",
                               color=discord.Color.teal())
    await ctx.reply(embed=withdrawem)


@bot.command(aliases=['dep'])
async def deposit(ctx, amount=None):
    await open_account(ctx.author)

    if amount == None:
        em = discord.Embed(title="Please enter an amount",
                           color=discord.Color.teal())
        await ctx.reply(embed=em)
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
        em = discord.Embed(title="You don't have that much money!",
                           color=discord.Color.teal())
        await ctx.reply(embed=em)
        return
    if amount < 0:
        em = discord.Embed(title="Amount must be positive!",
                           color=discord.Color.teal())
        await ctx.reply(embed=em)
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, 1 * amount, "Bank")
    await update_bank(ctx.author, -2 * amount, "Wallet")

    depositem = discord.Embed(title=f"You deposited {amount} coins!",
                              color=discord.Color.teal())
    await ctx.reply(embed=depositem)


async def update_bank(user, change=0, mode="Wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json", 'w') as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["Wallet"], users[str(user.id)]["Bank"]]
    return bal


@bot.command()
async def send(ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        em = discord.Embed(title="Please enter an amount",
                           color=discord.Color.teal())
        await ctx.reply(embed=em)
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
        em = discord.Embed(title="You don't have that much money!",
                           color=discord.Color.teal())
        await ctx.reply(embed=em)
        return
    if amount < 0:
        em = discord.Embed(title="Amount must be positive!",
                           color=discord.Color.teal())
        await ctx.reply(embed=em)
        return

    await update_bank(ctx.author, -1 * amount, "Bank")
    await update_bank(member, amount, "Wallet")

    depositem = discord.Embed(title=f"You gave {amount} coins!",
                              color=discord.Color.teal())
    await ctx.reply(embed=depositem)


@bot.command()
async def slots(ctx, amount=None):
    await open_account(ctx.author)

    if amount == None:
        em = discord.Embed(title="Please enter an amount",
                           color=discord.Color.teal())
        await ctx.reply(embed=em)
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
        em = discord.Embed(title="You don't have that much money!",
                           color=discord.Color.teal())
        await ctx.reply(embed=em)
        return
    if amount < 0:
        em = discord.Embed(title="Amount must be positive!",
                           color=discord.Color.teal())
        await ctx.reply(embed=em)
        return

    final = []
    for i in range(3):
        a = random.choice(["😂", "😊", "😢"])

        final.append(a)

    await ctx.reply("The slots are..." + str(final))

    if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
        await update_bank(ctx.author, 1 * amount)
        win = discord.Embed(title="You won!")
        await ctx.reply(embed=win)
    else:
        await update_bank(ctx.author, -2 * amount)
        lose = discord.Embed(title="You lost lol")
        await ctx.reply(embed=lose)


async def update_bank(user, change=0, mode="Wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json", 'w') as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["Wallet"], users[str(user.id)]["Bank"]]
    return bal


@bot.command()
async def shop(ctx):
    em = discord.Embed(title="BeeMod Economy Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name=name, value=f"${price} │ {desc}")
        em.set_footer(text="Use b!buy <item> to buy it!")

    await ctx.reply(embed=em)


@bot.command()
async def buy(ctx, item, amount=1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            em = discord.Embed(title="That item isn't in the shop!")
            await ctx.reply(embed=em)
            return
        if res[1] == 2:
            em2 = discord.Embed(
                title=
                f"You don't have enough money in your wallet to buy {amount} {item}"
            )
            await ctx.reply(embed=em2)
            return

    em3 = discord.Embed(title=f"You just bought {amount} {item}!")
    await ctx.reply(embed=em3)


@bot.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(50)

    begembed = discord.Embed(
        title=f"{ctx.author.name}",
        description=f"Someone gave you {earnings} coins! How lucky is that?",
        color=discord.Color.teal())

    await ctx.reply(embed=begembed)

    users[str(user.id)]["Wallet"] += earnings

    with open("bank.json", 'w') as f:
        json.dump(users, f)


@bot.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    em = discord.Embed(title="Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name=name, value=amount)

        await ctx.reply(embed=em)


@bot.command(aliases=["lb"])
async def leaderboard(ctx, x=3):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["Wallet"] + users[user]["Bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total, reverse=True)

    em = discord.Embed(
        title=f"Top {x} Richest People",
        description=
        "This is decided on the basis of raw money in the bank and wallet",
        color=discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        name = member.name
        em.add_field(name=f"{index}. {name}", value=f"{amt}", inline=False)
        if index == x:
            break
        else:
            index += 1

    await ctx.reply(embed=em)


async def buy_this(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0] < cost:
        return [False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["bag"] = [obj]

    with open("bank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost * -1, "Wallet")

    return [True, "Worked"]


keep_alive()
bot.run(TOKEN)
