@bot.command()
@commands.cooldown(1, 2629746, commands.BucketType.user)
async def monthly(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(2500)

    begembed = discord.Embed(title=f"{ctx.author.name}", description=f"Here, have {earnings} coins! It is your monthly gift after all", color=discord.Color.teal())

    await ctx.reply(embed=begembed)

    users[str(user.id)]["Wallet"] += earnings

    with open("bank.json", 'w') as f:
        json.dump(users, f)
