#!/usr/bin/python3
""" using an api with auth"""

import sys
import requests

if __name__ == '__main__':
    # Check if the correct number of arguments was provided
    if len(sys.argv) != 3:
        print('Usage: python3 github_id.py <username> <token>')
        sys.exit(1)

    # Get the username and personal access token from command line arguments
    username, token = sys.argv[1], sys.argv[2]

    # Set up the API endpoint and headers
    api_url = 'https://api.github.com/user'
    headers = {'Accept': 'application/vnd.github.v3+json'}

    # Authenticate using Basic Authentication with personal access token
    auth = (username, token)

    # Make the API request to get the user's id
    response = requests.get(api_url, headers=headers, auth=auth)

    # Check if the response was successful
    if response.status_code != 200:
        print(f'Request failed with status code {response.status_code}')
        sys.exit(1)

    # Extract the user's id from the response
    user_id = response.json().get('id')

    # Print the user's id
    print(f'Your GitHub user id is: {user_id}')
