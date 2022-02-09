@bot.command()
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        em = discord.Embed(title="Please enter an amount", color=discord.Color.teal())
        await ctx.reply(embed=em)
        return

    bal = await update_bank(ctx.author)

    amount=int(amount)
    if amount > bal[1]:
        em = discord.Embed(title="You don't have that much money!", color=discord.Color.teal())
        await ctx.reply(embed=em)
        return
    if amount < 0:
        em = discord.Embed(title="Amount must be positive!", color=discord.Color.teal())
        await ctx.reply(embed=em)
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"Bank")
    
    withdrawem = discord.Embed(title=f"You withdrew {amount} coins!", color=discord.Color.teal())
    await ctx.reply(embed=withdrawem)
