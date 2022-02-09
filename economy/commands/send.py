@bot.command()
async def send(ctx,member:discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)

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

    await update_bank(ctx.author,-1*amount,"Bank")
    await update_bank(member,amount,"Wallet")
    
    depositem = discord.Embed(title=f"You gave {amount} coins!", color=discord.Color.teal())
    await ctx.reply(embed=depositem)
