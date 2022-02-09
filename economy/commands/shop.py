mainshop = [{"name":"Pencil","price":20,"description":"Write/Draw something"},
{"name":"Watch","price":500,"description":"Check the time"},
{"name":"iPhone","price":1000,"description":"Call people and use apps"},
{"name":"iPad","price":2000,"description":"Use apps"},
{"name":"Laptop","price":3000,"description":"Do work and play games"},
{"name":"Gaming PC","price":5000,"description":"Stream to Twitch and play games"}]

@bot.command()
async def shop(ctx):
    em = discord.Embed(title="BeeMod Economy Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} │ {desc}")
        em.set_footer(text="Use b!buy <item> to buy it!")
    
    await ctx.reply(embed=em)
