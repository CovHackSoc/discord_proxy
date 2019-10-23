async def reload(ctx):
    await ctx.send('reload')

export = [{
    'name': 'reload',
    'function': reload,
    'admin': True
}]
