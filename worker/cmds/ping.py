async def ping(ctx):
    await ctx.send('{.author.mention} pong'.format(ctx))

export = [{
    'name': 'ping',
    'function': ping
}]
