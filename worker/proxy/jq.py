# Proxy that uses pyjq to extract data from random apis.

import requests
import pyjq as jq

def jq_proxy(url, jq_string):
    def jq_handler(ctx):
        r = requests.get(url)
        return jq.all(jq_string, r.json())

    return jq_handler
