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
![image](https://user-images.githubusercontent.com/88248957/149185021-b54f0ab0-a6ff-4c47-8e72-04b60dde2b81.png)

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
    activity = discord.Game(name="b!help", type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
```
![image](https://user-images.githubusercontent.com/88248957/149186988-722e31ec-528a-415e-b7b7-b1a41965b77d.png)

To see similiar projects, visit my website
  https://skellyy.repl.co
