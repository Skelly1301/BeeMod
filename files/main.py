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

bot = commands.Bot(command_prefix='b!')
bot.remove_command ('help')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord, lol')
    activity = discord.Activity(type=discord.ActivityType.watching, name=str(len(bot.guilds)) + " servers! " + " | b!help ")
    await bot.change_presence(status=discord.Status.online, activity=activity)



#moderation

@bot.command(brief="Bans a server member", description="b!ban <member> [reason]")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
      await member.ban(reason=reason)
      await ctx.reply(f'User {member} has been banned.')
    except:
      await ctx.reply("The bot has missing permissions\n\nMake sure the Bot's top-most role is above the member's top-most role (the member who you are going to ban)")

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

@bot.command(brief="Kicks a server member", description="b!kick <member> [reason]")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
      await member.kick(reason=reason)
      await ctx.reply(f'User {member} has been kicked.')
    except:
      await ctx.reply("The bot has missing permissions\n\nMake sure the Bot's top-most role is above the member's top-most role (the member who you are going to kick)")

@bot.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.MissingPermissions):
    await ctx.reply("You don't have the permissions to do that")
  elif isinstance(error,commands.MissingRequiredArgument):
    await ctx.reply("You don't have the permissions to do that")
  else:
      print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
      traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


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

    msg = "\n".join([f"cleared {amount} messages sent by {author}" for author,
                     amount in authors.items()])
    await ctx.channel.send(msg, delete_after=7)

#fun

@bot.command(aliases=['8ball', '8b'])
async def _8ball(ctx):
  responses = [
        'Hell no.',
        'Probably not.',
        'Idk bro.',
        'Probably.',
        'Hell yeah my dude.',
        'It is certain.',
        'It is decidedly so.',
        'Without a Doubt.',
        'Yes - Definitely.',
        'You may rely on it.',
        'As i see it, Yes.',
        'Most Likely.',
        'Outlook Good.',
        'Yes!',
        'No!',
        'Signs a point to Yes!',
        'Reply Hazy, Try again.',
        'IDK but I do know that you should click this link https://skellyy.repl.co',
        'Better not tell you know.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't Count on it.",
        'My reply is No.',
        'My sources say No.',
        'Outlook not so good.',
        'Very Doubtful']
  await ctx.reply(f'{random.choice(responses)}')


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']
  json_data[0]['a']
  return(quote)

@bot.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.reply(quote)

@bot.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)

@bot.command()
async def rps(ctx, message):
    answer = message.lower()
    choices = ["rock", "paper", "scissors"]
    computers_answer = random.choice(choices)
    if answer not in choices:
        await ctx.reply ("That is not a valid option. Please use rock, paper or scissors")
        return
    else:
        if computers_answer == answer:
            await ctx.reply(f"Tie! We both picked {answer}")
        if computers_answer == "rock":
            if answer == "paper":
                await ctx.reply(f"You win! I picked {computers_answer} and you picked {answer}!")
        if computers_answer == "paper":
            if answer == "rock":
                await ctx.reply(f"I win! I picked {computers_answer} and you picked {answer}!")
        if computers_answer == "scissors":
            if answer == "rock":
                await ctx.reply(f"You win! I picked {computers_answer} and you picked {answer}!")
        if computers_answer == "rock":
            if answer == "scissors":
                await ctx.reply(f"I win! I picked {computers_answer} and you picked {answer}!")
        if computers_answer == "paper":
            if answer == "scissors":
                await ctx.reply(f"You win! I picked {computers_answer} and you picked {answer}!")
        if computers_answer == "scissors":
            if answer == "paper":
                await ctx.reply(f"I win! I picked {computers_answer} and you picked {answer}!")

#help

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
    embed.add_field(name="b!meme", value="Reddit memes in discord", inline=True)
    embed.add_field(name="b!rps", value="Use b!rps <choice> and see who wins, you or BeeMod!", inline=True)

    embed.add_field(name="ㅤ", value="ㅤ", inline=False)

    embed.add_field(name="UTILITIES", value="ㅤ", inline=False)

    embed.add_field(name="b!gstart", value="Start a giveaway! Use !gstart <how many minutes you want it to last> <prize>",inline=True)
    embed.add_field(name="b!lvl", value="See your server level!",inline=True)
    
    embed.add_field(name="ㅤ", value="ㅤ", inline=False)

    embed.add_field(name="OTHER", value="ㅤ", inline=False)

    embed.add_field(name="b!servers", value="Shows how manys servers the bot is in.",inline=True)
    embed.add_field(name="b!website", value="Shows the bots website.", inline=True)

    embed.set_footer(text="Made by Skelly b!credits")
    
    await ctx.reply(embed=embed)



#other

@bot.command(brief="Bot website")
async def website(ctx):
    await ctx.reply("https://beemodweb.skellyy.repl.co")


@bot.command(brief="Server list", description="Shows how many servers the bot is in")
async def servers(ctx):
    await ctx.reply("I'm in " + str(len(bot.guilds)) + " servers!")

@bot.command()
async def credits(ctx):
    embed=discord.Embed(title="Credits", description="All of the people who have helped make BeeMod", color=0x109319)

    embed.set_author(name="BeeMod", icon_url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")

    embed.add_field(name="Skelly", value="Created the bot, and has coded all the commands (so far)", inline=False)

    embed.set_footer(text="I am not lonely dw")
    
    await ctx.reply(embed=embed)



#giveaway

@bot.command()
@commands.has_permissions(manage_messages=True)
async def gstart(ctx, mins : int, * , prize: str):
    embed = discord.Embed(title = "Giveaway Time! 🎉", description = f"{prize}", color = ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)

    embed.add_field(name = "Ends at:", value = f"{end} UTC")
    embed.set_footer(text = f"Ends in {mins}")

    my_msg = await ctx.reply(embed = embed)


    await my_msg.add_reaction("🎉")


    await asyncio.sleep(mins*60)


    new_msg = await ctx.channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}")




#leveling




@bot.event
async def on_message(message):
    if not message.author.bot:
        print('function load')
        with open('level.json','r') as f:
            users = json.load(f)
            print('file load')
        await update_data(users, message.author,message.guild)
        await add_experience(users, message.author, 4, message.guild)
        await level_up(users, message.author,message.channel, message.guild)

        with open('level.json','w') as f:
            json.dump(users, f)
    await bot.process_commands(message)



async def update_data(users, user,server):
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
  lvl_end = int(experience ** (1/4))
  if str(user.guild.id) != '757383943116030074':
    if lvl_start < lvl_end:
      await channel.send('{} has reached level **{}**. GG!'.format(user.mention, lvl_end))
      users[str(user.guild.id)][str(user.id)]['level'] = lvl_end


@bot.command(aliases = ['rank','lvl'])
async def level(ctx,member: discord.Member = None):

    if not member:
        user = ctx.message.author
        with open('level.json','r') as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(user.id)]['level']
        exp = users[str(ctx.guild.id)][str(user.id)]['experience']

        embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP " ,color = discord.Color.green())
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
    else:
      with open('level.json','r') as f:
          users = json.load(f)
      lvl = users[str(ctx.guild.id)][str(member.id)]['level']
      exp = users[str(ctx.guild.id)][str(member.id)]['experience']
      embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP" ,color = discord.Color.green())
      embed.set_author(name = member, icon_url = member.avatar_url)

      await ctx.send(embed = embed)









keep_alive()
bot.run(TOKEN)
