from discord.ext import commands
import importlib

import cmds
from checks.check_role import check_role

class DiscordProxy:

    def __init__(self, key, admin_role='bot_admin'):
        self.discord_key = key
        self.bot = commands.Bot(command_prefix='!')
        self.admin_role

    def _load_checks(self, cmd):
        checks = []
        if cmd.get('admin', None) is True:
            checks.append(check_role(self.admin_role))

    def _load_internal_commands(self):
        # add all of the predefined commands to the bot.
        all_cmds = []
        for cmd in cmds.__all__:
            all_cmds += importlib.import_module('cmds.{}'.format(cmd)).export
        for cmd in all_cmds:
            self._load_checks(cmd)

            new_cmd = commands.Command(
                cmd['function'],
                name=cmd['name'],
                checks=checks
            )
            self.bot.add_command(new_cmd)


    def start(self):
        self._load_internal_commands()
        self.bot.run(self.discord_key)
