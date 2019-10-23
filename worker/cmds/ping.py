async def ping(ctx):
    await ctx.send('pong')

export = [{
    'name': 'ping',
    'function': ping
}]
