@bot.command()
async def rps(ctx, message):
    answer = message.lower()
    choices = ["rock", "paper", "scissors"]
    computers_answer = random.choice(choices)
    if answer not in choices:
        await ctx.reply ("That is not a valid option. Please use rock, paper or scissors")
        return
    else:
        if computers_answer == answer:
            await ctx.reply(f"Tie! We both picked {answer}")
        if computers_answer == "rock":
            if answer == "paper":
                await ctx.reply(f"You win! I picked {computers_answer} and you picked {answer}!")
        if computers_answer == "paper":
            if answer == "rock":
                await ctx.reply(f"I win! I picked {computers_answer} and you picked {answer}!")
        if computers_answer == "scissors":
            if answer == "rock":
                await ctx.reply(f"You win! I picked {computers_answer} and you picked {answer}!")
        if computers_answer == "rock":
            if answer == "scissors":
                await ctx.reply(f"I win! I picked {computers_answer} and you picked {answer}!")
        if computers_answer == "paper":
            if answer == "scissors":
                await ctx.reply(f"You win! I picked {computers_answer} and you picked {answer}!")
        if computers_answer == "scissors":
            if answer == "paper":
                await ctx.reply(f"I win! I picked {computers_answer} and you picked {answer}!")
