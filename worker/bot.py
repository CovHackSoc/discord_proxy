from discord.ext import commands
import cmds
import importlib

class DiscordProxy:

    def __init__(self, key):
        self.discord_key = key
        self.bot = commands.Bot(command_prefix='!')
        # add all of the predefined commands to the bot.
        all_cmds = []
        for cmd in cmds.__all__:
            all_cmds += importlib.import_module('cmds.{}'.format(cmd)).export
        for cmd in all_cmds:
            new_cmd = commands.Command(
                cmd['function'],
                name=cmd['name'],
            )
            self.bot.add_command(new_cmd)

    def start(self):
        self.bot.run(self.discord_key)
