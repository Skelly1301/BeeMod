@bot.command(brief="Bans a server member", description="b!ban <member> [reason]")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member} has been banned.')
