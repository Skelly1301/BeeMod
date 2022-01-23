@bot.command(brief="Kicks a server member", description="b!kick <member> [reason]")
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked.')
