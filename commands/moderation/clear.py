@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    authors = {}
    async for message in ctx.channel.history(limit=amount + 1):
        if message.author not in authors:
            authors[message.author] = 1
        else:
            authors[message.author] += 1
        await message.delete()

    msg = "\n".join([f"cleared {amount} messages sent by {author}" for author,
                     amount in authors.items()])
    await ctx.channel.send(msg, delete_after=7)
