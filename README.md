# discord_proxy

Exposes web services over Discord

## Development Setup

Get the dependencies installed in a virtual environment:

```bash
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Now follow the instructions here to get your own API key:

https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token

Take that API key and export it into your development environment like so:

```bash
export DISCORD_KEY='YOUR KEY HERE'
```

You can now run the project via several means:

* Using the Heroku cli with `heroku local`
* With Foreman https://github.com/ddollar/foreman
* Or just by running `python worker`


## Adding new commands

Create a new file in `worker/cmds` and define a function like so:

```python
async def ping(ctx):
    await ctx.send('pong')
```

Then define an export dictionary like so:

```python
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

## Adding new API commands

If you are just adding support for new commands that call an HTTP API that
returns JSON, you have two options:

* The jq interface for APIs you don't control. Doesn't currently support POST.
* The standard interface if you can modify what the endpoint returns. POSTs details to the endpoint in a standard form.

After you get your response, you can define how you would like it to be
displayed with a python format string.

We use `API_LIST_URL` to host the configuration for this.

### JQ interface

These uses [JQ](https://stedolan.github.io/jq/) to extract data from a response.

### Standard interface

## Security

Commands loaded are mostly trusted, though it's probably worth checking how I
load responses etc. I'm not sure how we format responses is safe.

We're running this on private discords with users we trust, so consider that
before using this.

## Configuration

You can find an example of the API config in `examples/config.json`

An overview of the environment variables used:
* DISCORD_KEY - Your discord bot API key
* ADMIN_ROLE - Role to check if a user has before running privileged commands
* API_LIST_URL - Where to fetch the API config from. In dev, I'm using JSONBin.
