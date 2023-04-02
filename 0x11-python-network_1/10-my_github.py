#!/usr/bin/python3
"""
Takes your Github credentials and uses the Github API to display your id.
"""

import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    headers = {'Accept': 'application/vnd.github.v3+json'}

    response = requests.get(url, headers=headers, auth=(username, password))
    data = response.json()

    print(data.get('id'))
