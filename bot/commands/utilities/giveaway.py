@bot.command()
@commands.has_permissions(manage_messages=True)
async def gstart(ctx, mins : int, * , prize: str):
    embed = discord.Embed(title = "Giveaway Time! 🎉", description = f"{prize}", color = ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)

    embed.add_field(name = "Ends at:", value = f"{end} UTC")
    embed.set_footer(text = f"Ends in {mins}")

    my_msg = await ctx.reply(embed = embed)


    await my_msg.add_reaction("🎉")


    await asyncio.sleep(mins*60)


    new_msg = await ctx.channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}")
