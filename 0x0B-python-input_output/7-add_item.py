#!/usr/bin/python3

"""Add all arguments to a Python list and save them to a file."""

import sys
import json

def save_to_json_file(my_obj, filename):
    """Save a python object to a json file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
        
def load_from_json_file(filename):
    """Load python object from a json file"""
    with open(filename, 'r') as f:
        return json.load(f)
    
args = sys.argv[1:]

if args:
    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []
    items += args
    save_to_json_file(items, 'add_item.json')
else:
    print("No arguments provided.")
