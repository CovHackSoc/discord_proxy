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
