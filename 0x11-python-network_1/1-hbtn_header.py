#!/usr/bin/python3

"""Module to get the value of X-Request-Id header"""

import sys
import urllib.request


def get_request_id(url: str) -> str:
    """
    Get the value of X-Request-Id header
    Args: url (str): URL to send the request
    Request: str: Value of the X-Rquest_Id header in the response
    """

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        headers = res.info()
        x_request_id = headers.get('X-Request-Id')
        return x_request_id


if __name__ == '__main__':
    url = sys.argv[1]
    x_request_id = get_request_id(url)
    print(x_request_id)
