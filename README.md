# discord_proxy
Exposes web services over Discord

## Development Setup

Get the dependencies installed in a virtual environment:

```
virtualenv -p python3 .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Now follow the instructions here to get your own API key:

https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token

Take that API key and export it into your development environment like so:

```
export DISCORD_KEY='YOUR KEY HERE'
```

You can now run the project via several means:

* Using the Heroku cli with `heroku local`
* With Foreman https://github.com/ddollar/foreman
* Or just by running `python worker`


## Adding new commands

Create a new file in `worker/cmds` and define a function like so:

```
async def ping(ctx):
    await ctx.send('pong')
```

Then define an export dictionary like so:

```
export = [{
    'name': 'ping',
    'function': ping,
    'admin': False
}]
```

You can define multiple functions in the same file, just make sure you just put
it's export dictionary in the list!

If you want your command to be usable by only people with the bot_admin group,
just set admin to true.
