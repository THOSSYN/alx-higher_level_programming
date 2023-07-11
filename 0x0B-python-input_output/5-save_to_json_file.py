#!/usr/bin/python3
"""Saves object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file, using a
       JSON representation

       Args:
        my_obj: is the json obj to be saved
        filename: is the name of the file tosave object to
    """
    with open(filename, mode='w') as a_file:
        return json.dump(my_obj, a_file)
