@bot.command()
async def news(ctx):
    em = discord.Embed(title="BeeMod Updates & News",
                       description="All the latest updates and news on BeeMod")

    em.set_author(
        name="BeeMod v1.1",
        icon_url=
        "https://media.discordapp.net/attachments/821782050649800705/933773030809796638/mcbee.jpg?width=586&height=586"
    )

    em.add_field(name="Added b!lb command", value="v1.0.9", inline=False)
    em.add_field(
        name=
        "Finished BeeMods economy system! (First part) second part coming soon!",
        value="v1.1",
        inline=False)

    await ctx.reply(embed=em)
