#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """a function that deletes a key in a dictionary.

       Args:
        first arg: a_dictionary
        second arg: key=""
    """
    dlete_key = []

    for x, y in a_dictionary.items():
        if x == key:
            dlete_key.append(x)
    for item in dlete_key:
        del a_dictionary[item]
    return a_dictionary
