#!/usr/bin/python3
"""
This script takes in a URL as a command line argument,
sends a request to the URL and
displays the body of the response (decoded in utf-8).
It also handles HTTPError exceptions
and prints out the error code.
"""

from urllib.error import HTTPError
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(argv) != 2:
        print(f"Usage: python3 {argv[0]} <URL>")
        exit(1)

    # Get the URL from command line arguments
    url = argv[1]

    try:
        # Send a request to the URL
        with urlopen(url) as response:
            # Display the body of the response decoded in utf-8
            print(response.read().decode("utf-8"))

    # Handle HTTPError exceptions
    except HTTPError as error:
        # Print out the error code
        print(f"Error code: {error.status}")
