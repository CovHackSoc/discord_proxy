import os

from bot import DiscordProxy

from dotenv import load_dotenv
load_dotenv()


if __name__ == '__main__':
    inst = DiscordProxy(os.environ['DISCORD_KEY'], os.environ['ADMIN_ROLE'])
    inst.start()
