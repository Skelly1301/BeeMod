@bot.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.MissingPermissions):
    await ctx.send("You don't have the permissions to do that")
  elif isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("You don't have the permissions to do that")
