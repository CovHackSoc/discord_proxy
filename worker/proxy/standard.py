# Standard Proxy for things that implement our spec.

import json
import requests

def standard_proxy(url, meta):
    def standard_handler(ctx, args):
        # What we send to the API
        data = {
            'message': {
                'content': ctx.message.content,
                'args': args
            },
            'channel': {
                'name': ctx.channel.name,
                'id': ctx.channel.id,
                'topic': ctx.channel.topic
            },
            'author': {
                'name': ctx.author.name,
                'id': ctx.author.id,
                'mention': ctx.author.mention
            },
            'server': {
                'name': ctx.guild.name,
                'id': ctx.guild.id
            }
        }
        r = requests.post(url, data=data)
        return r.json()

    return standard_handler
