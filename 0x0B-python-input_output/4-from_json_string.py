#!/usr/bin/python3
"""From Json String to object"""

import json


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
       represented by a JSON string:

       Args:
        my_str: is the string to be converted
    """
    return json.loads(my_str)
