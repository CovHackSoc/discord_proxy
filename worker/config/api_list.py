# Load in the new methods defined 

from discord.ext import commands
import requests


from proxy.jq import jq_proxy
from proxy.standard import standard_proxy

def formatter(format_str, func):
    async def formatter_handler(ctx):
        data = func(ctx)
        for item in data:
            await ctx.send(format_str.format(**item))
    return formatter_handler

def make_command(endpoint):
    # check the type of this endpoint
    resp = None
    if endpoint['type'] == 'jq':
        resp = jq_proxy(endpoint['url'], endpoint['meta'])
    else:
        resp = standard_proxy(endpoint['url'], endpoint['meta'])

    return formatter(endpoint['format'], resp)

def api_list(bot, url):
    r = requests.get(url)
    resp = r.json()
    for endpoint in resp:
        function = make_command(endpoint)
        new_cmd = commands.Command(
            function,
            name=endpoint['name']
        )
        bot.add_command(new_cmd)
