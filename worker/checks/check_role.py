# Stolen from https://github.com/Rapptz/discord.py/blob/4c3e53edf4ff90e3fcf195c429601a553d661cd8/discord/ext/commands/core.py
# due to it being a pain to just extract it from the decorator.

import discord
from discord.ext.commands.errors import *

def check_role(item):
    def predicate(ctx):
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            raise NoPrivateMessage()

        if isinstance(item, int):
            role = discord.utils.get(ctx.author.roles, id=item)
        else:
            role = discord.utils.get(ctx.author.roles, name=item)
        if role is None:
                raise MissingRole(item)
        return True
    return predicate

