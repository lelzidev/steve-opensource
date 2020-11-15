@client.command(name='dice')
@commands.guild_only()
async def roll_the_dice(ctx):
    response = [
        'Your answer is 1!',
        'Your answer is 2!',
        'Your answer is 3!',
        'Your answer is 4!',
        'Your answer is 5!',
        'Your answer is 6!',
    ]

    await ctx.send(random.choice(response))
