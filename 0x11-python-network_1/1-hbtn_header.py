#!/usr/bin/python3
""" a script that takes in a URL, sends a request
to the URL and display the value of the X-Requested-Id
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    print(response.headers.get("X-Request-Id"))
