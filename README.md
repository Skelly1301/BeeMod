# 🐝 BeeMod
  **Please note the code is updated regularly, but the Readme is not always up-to-date. If anything seems off, thats why**
  
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/Skelly1301/BeeMod)
![GitHub last commit](https://img.shields.io/github/last-commit/Skelly1301/BeeMod)
![GitHub language count](https://img.shields.io/github/languages/count/Skelly1301/BeeMod)
![GitHub top language](https://img.shields.io/github/languages/top/Skelly1301/BeeMod)
![Lines of code](https://img.shields.io/tokei/lines/github/skelly1301/beemod)
![GitHub repo size](https://img.shields.io/github/repo-size/skelly1301/beemod)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/skelly1301/beemod)

The code and info on my discord bot, hosted in the cloud, coded in repl.it

**Please make sure you check the [import list](https://github.com/Skelly1301/BeeMod/blob/main/files/imports/import%20list.py) for all the imports needed for ALL the commands the work.**

## All commands
[Ban member](https://github.com/Skelly1301/BeeMod/blob/main/commands/moderation/ban%20member.py), [Kick member](https://github.com/Skelly1301/BeeMod/blob/main/commands/moderation/kick%20member.py), [Unban member](https://github.com/Skelly1301/BeeMod/blob/main/commands/moderation/unban%20member.py), [Meme](https://github.com/Skelly1301/BeeMod/blob/main/commands/fun/meme.py), [Clear](https://github.com/Skelly1301/BeeMod/blob/main/commands/moderation/clear.py), [Inspire](https://github.com/Skelly1301/BeeMod/blob/main/commands/fun/8ball.py), [8ball](https://github.com/Skelly1301/BeeMod/blob/main/commands/fun/8ball.py), [Servers](https://github.com/Skelly1301/BeeMod/blob/main/commands/info/servers.py), [Website](https://github.com/Skelly1301/BeeMod/blob/main/commands/info/website.py), [Rock Paper Scissors (rps)](https://github.com/Skelly1301/BeeMod/blob/main/commands/fun/rps.py).
## Moderation
### Kick function
![image](https://user-images.githubusercontent.com/88248957/149184158-5189fec1-bfd7-401b-b079-cd0284f7e411.png)

Simple kick member function, just use b!kick <member> [reason]

### Ban function
![image](https://user-images.githubusercontent.com/88248957/149184813-370674a0-595a-45e2-bc88-c74307e42e37.png)

Simple ban member function, just use b!ban <member> [reason]

## Help
![image](https://user-images.githubusercontent.com/88248957/150985101-be19701c-05f0-430e-8f74-4047993cc6d8.png)

Simple help member function, just use b!help
  
## Fun
### 8ball
![image](https://user-images.githubusercontent.com/88248957/150986907-a96a83cf-0acd-4de7-862c-a17b3caa83b3.png)

### Inspire
![image](https://user-images.githubusercontent.com/88248957/150987015-762ef3aa-3a27-4eaf-946d-bdfda85120e2.png)
![image](https://user-images.githubusercontent.com/88248957/150987109-60219a7d-f565-4421-a6db-56875582cb36.png)
![image](https://user-images.githubusercontent.com/88248957/150987227-dfad8831-8ae6-4425-b2fb-07e9a1e7a549.png)

  Made using [zenquotes.io](https://zenquotes.io)

### Meme
![image](https://user-images.githubusercontent.com/88248957/151582479-8befa569-f42b-48b8-8dba-f400d0a8cdfe.png)

  Sends a random meme from reddit, in discord.
  
## Code
### Simple command code
```python
@bot.command()
async def ping(ctx):
    await ctx.send("pong!")
```
When the user types b!ping, the bot will reply with, pong!
  
### Changing bot status
This will set the bots status to 'Playing b!help' and will set the online status to do not disturb (dnd)
```python
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord, lol')
    activity = discord.Game(name="b!help | " + str(len(bot.guilds)) + " servers!")
    await bot.change_presence(status=discord.Status.online, activity=activity)
```
![image](https://user-images.githubusercontent.com/88248957/150197391-1b3c39d6-2634-42c8-a542-c1b1e1a9e10f.png)

[Bot website](https://beemodweb.skellyy.repl.co)
  
To see similiar projects, visit [my website](https://skellyy.repl.co)
