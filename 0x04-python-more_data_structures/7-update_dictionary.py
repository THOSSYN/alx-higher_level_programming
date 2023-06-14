#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """a function that replaces or adds key/value
       in a dictionary.

       Args:
        first arg: a_dictionary
        second arg: key
        third arg: value
    """
    a_dictionary[key] = value
    return a_dictionary
