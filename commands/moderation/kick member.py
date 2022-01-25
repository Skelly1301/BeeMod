@bot.command(brief="Kicks a server member", description="b!kick <member> [reason]")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
      await member.kick(reason=reason)
      await ctx.send(f'User {member} has been kicked.')
    except:
      await ctx.send("The bot has missing permissions\n\nMake sure the Bot's top-most role is above the member's top-most role (the member who you are going to kick)")
