import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx, *args):
    await ctx.send('pong')

if __name__ == '__main__':
    bot.run(os.environ['DISCORD_KEY'])
