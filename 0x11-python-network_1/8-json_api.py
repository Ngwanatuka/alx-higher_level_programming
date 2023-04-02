#!/usr/bin/python3
"""
    Sends a POST request with a letter as a parameter and
    displays the response in a particular format.
"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": letter})

    try:
        response_dict = response.json()
        if response_dict:
            print("[{}] {}".format(
                response_dict.get('id'), response_dict.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
