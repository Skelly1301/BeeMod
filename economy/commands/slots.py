@bot.command()
async def slots(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        em = discord.Embed(title="Please enter an amount", color=discord.Color.teal())
        await ctx.reply(embed=em)
        return

    bal = await update_bank(ctx.author)

    amount=int(amount)
    if amount > bal[0]:
        em = discord.Embed(title="You don't have that much money!", color=discord.Color.teal())
        await ctx.reply(embed=em)
        return
    if amount < 0:
        em = discord.Embed(title="Amount must be positive!", color=discord.Color.teal())
        await ctx.reply(embed=em)
        return

    final = []
    for i in range(3):
        a = random.choice(["😂", "😊", "😢"])

        final.append(a)

    await ctx.reply("The slots are..." + str(final))

    if final[0] == final [1] or final[0] == final [2] or final[2] == final [1]:
        await update_bank(ctx.author,1*amount)
        win = discord.Embed(title="You won!")
        await ctx.reply(embed=win)
    else:
        await update_bank(ctx.author,-2*amount) 
        lose = discord.Embed(title="You lost lol")
        await ctx.reply(embed=lose)
