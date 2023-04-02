#!/usr/bin/python3
"""
Fetches the body of a URL and displays it.
If an HTTPS error occurs, display the error code.
"""

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))

    else:
        print(response.text)
