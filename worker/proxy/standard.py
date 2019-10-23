# Standard Proxy for things that implement our spec.

import json
import requests

def standard_proxy(url, meta):
    def standard_handler(ctx):
        pass
    return standard_handler
