# BeeMod
The code and info on my discord bot, hosted in the cloud, coded in repl.it



## Moderation
### Kick function
![image](https://user-images.githubusercontent.com/88248957/149184158-5189fec1-bfd7-401b-b079-cd0284f7e411.png)

Simple kick member function, just use b!kick <member> [reason]

### Ban function
![image](https://user-images.githubusercontent.com/88248957/149184813-370674a0-595a-45e2-bc88-c74307e42e37.png)

Simple ban member function, just use b!ban <member> [reason]

### Help function
![image](https://user-images.githubusercontent.com/88248957/150682301-ca9c2637-b326-4a61-8e3e-26cc8900319d.png)

Simple help member function, just use b!help
  
  
  
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

To see similiar projects, visit my website
  https://skellyy.repl.co
