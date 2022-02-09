@bot.command(aliases=['dep'])
async def deposit(ctx,amount = None):
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

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,1*amount,"Bank")
    await update_bank(ctx.author,-2*amount,"Wallet")
    
    depositem = discord.Embed(title=f"You deposited {amount} coins!", color=discord.Color.teal())
    await ctx.reply(embed=depositem)

async def update_bank(user,change = 0,mode = "Wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json", 'w') as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["Wallet"],users[str(user.id)]["Bank"]]
    return bal
