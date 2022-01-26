import os
from keep_alive import keep_alive
from discord.ext import commands
import discord
from dotenv import load_dotenv
import random
import requests
import json

load_dotenv()
TOKEN = os.getenv('TOKEN')
client = discord.Client()

bot = commands.Bot(command_prefix='b!')
bot.remove_command ('help')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord, lol')
    activity = discord.Game(name="b!help | " + str(len(bot.guilds)) + " servers!")
    await bot.change_presence(status=discord.Status.online, activity=activity)



#moderation

@bot.command(brief="Bans a server member", description="b!ban <member> [reason]")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
      await member.ban(reason=reason)
      await ctx.send(f'User {member} has been banned.')
    except:
      await ctx.send("The bot has missing permissions\n\nMake sure the Bot's top-most role is above the member's top-most role (the member who you are going to ban)")

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
            await ctx.send(f'Unbanned {user.mention}')
            return

@bot.command(brief="Kicks a server member", description="b!kick <member> [reason]")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
      await member.kick(reason=reason)
      await ctx.send(f'User {member} has been kicked.')
    except:
      await ctx.send("The bot has missing permissions\n\nMake sure the Bot's top-most role is above the member's top-most role (the member who you are going to kick)")

@bot.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.MissingPermissions):
    await ctx.send("You don't have the permissions to do that")
  elif isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("You don't have the permissions to do that")


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
  await ctx.send(f'{random.choice(responses)}')


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']
  json_data[0]['a']
  return(quote)

@bot.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)



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
    
    embed.add_field(name="ㅤ", value="ㅤ", inline=False)

    embed.add_field(name="OTHER", value="ㅤ", inline=False)

    embed.add_field(name="b!servers", value="Shows how manys servers the bot is in.",inline=True)
    embed.add_field(name="b!website", value="Shows the bots website.", inline=True)

    embed.set_footer(text="Made by Skelly b!credits")
    
    await ctx.send(embed=embed)



#other

@bot.command(brief="Bot website")
async def website(ctx):
    await ctx.send("https://beemodweb.skellyy.repl.co")


@bot.command(brief="Server list", description="Shows how many servers the bot is in")
async def servers(ctx):
    await ctx.send("I'm in " + str(len(bot.guilds)) + " servers!")

@bot.command()
async def credits(ctx):
    embed=discord.Embed(title="Credits", description="All of the people who have helped make BeeMod", color=0x109319)

    embed.set_author(name="BeeMod", icon_url="https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586")

    embed.add_field(name="Skelly", value="Created the bot, and has coded all the commands (so far)", inline=False)

    embed.set_footer(text="I am not lonely dw")
    
    await ctx.send(embed=embed)

keep_alive()
bot.run(TOKEN)
