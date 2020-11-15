@client.command()
@commands.guild_only()
async def ping(ctx):
    embed = discord.Embed(colour=discord.Colour.green())
    embed.set_author(
        name='Ping Command')
    embed.add_field(
        name=f'{round (client.latency * 1000)}ms ',
        value='Gives the ping between the bot and the Discord API. this is calculated in MS(Micro seconds) and may differ each time.',
        inline=False)
    await ctx.send(embed=embed)
