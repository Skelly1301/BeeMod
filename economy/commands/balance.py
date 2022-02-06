async def get_bank_data():
    with open("bank.json", 'r') as f:
        users = json.load(f)
    return users

@bot.command(aliases=['bal'])
async def balance(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["Wallet"]
    bank_amt = users[str(user.id)]["Bank"]

    em = discord.Embed(title=f"{ctx.author.name}'s balance.", color=discord.Color.teal())
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name="Bank Balance", value=bank_amt)
    await ctx.send(embed=em)
