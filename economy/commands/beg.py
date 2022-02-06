@bot.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(50)

    begembed = discord.Embed(title=f"{ctx.author.name}", description=f"Someone gave you {earnings} coins! How lucky is that?", color=discord.Color.teal())

    await ctx.reply(embed=begembed)

    users[str(user.id)]["Wallet"] += earnings

    with open("bank.json", 'w') as f:
        json.dump(users, f)
