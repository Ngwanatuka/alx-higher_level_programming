#!/usr/bin/python3

""" A script that sends a POST request to a URL with an
email and displays the body of the response
"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email})
    data = data.encode("ascii")

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
