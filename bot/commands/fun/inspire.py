def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    json_data[0]['a']
    return (quote)

@bot.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.reply(quote)
