#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL,
and displays the X-Request-Id in the response.
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    header_value = response.headers.get("X-Request-Id")
    print(header_value)
