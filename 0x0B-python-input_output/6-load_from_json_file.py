#!/usr/bin/python3
"""Create object from a JSON file"""

import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”

       Args:
        filename: is the file to work on
    """
    with open(filename, mode='r') as f:
        return json.load(f)
