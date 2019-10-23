from discord.ext import commands
import importlib

import cmds
from checks.check_role import check_role
from config.api_list import api_list

class DiscordProxy:

    def __init__(self, key, api_list_url=None, admin_role='bot_admin'):
        self.discord_key = key
        self.bot = commands.Bot(command_prefix='!')
        self.admin_role = admin_role
        self.api_list_url = api_list_url

    def _load_checks(self, cmd):
        checks = []
        if cmd.get('admin', None) is True:
            checks.append(check_role(self.admin_role))
        return checks

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
                checks=self._load_checks(cmd)
            )
            self.bot.add_command(new_cmd)

    def _load_http_commands(self):
        # Call the loader.
        api_list(self.bot, self.api_list_url)

    def start(self):
        self._load_internal_commands()
        self._load_http_commands()
        self.bot.run(self.discord_key)
