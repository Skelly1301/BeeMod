@bot.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            em = discord.Embed(title="That item isn't in the shop!")
            await ctx.reply(embed=em)
            return
        if res[1]==2:
            em2 = discord.Embed(title=f"You don't have enough money in your wallet to buy {amount} {item}")
            await ctx.reply(embed=em2)
            return
    
    em3 = discord.Embed(title=f"You just bought {amount} {item}!")
    await ctx.reply(embed=em3)
