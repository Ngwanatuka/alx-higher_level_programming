#!/usr/bin/python3
"""
Sens a POST request with a letter as a parameter and
displays the response in a particular format.
"""

import sys
import requests


if __name__ == '__mian__':
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    url = "http://26550f78c48a.50da2fcc.alx-cod.online:5000/search_user"
    response = request.post(url, data={"q": letter})

    try:
        reponse_dict = response.json()
        if response_dict:
            print("[{}] {}".format(
                response_dict.get('id'), response_dict.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
