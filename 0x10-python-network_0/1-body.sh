#!/bin/bash

# Take in URL as argument
url="$1"

# Send GET request using curl and display response body
curl -sL "$url"

# Print "Route 2"
echo "Route 2"
