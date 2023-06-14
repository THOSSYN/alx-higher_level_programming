#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """a function that deletes keys with a
       specific value in a dictionary.

       Args:
        first arg: a_dictionary
        second arg: value
    """
    item_to_erase = []

    for x, y in a_dictionary.items():
        if y == value:
            item_to_erase.append(x)

    for x in item_to_erase:
        del a_dictionary[x]
    return a_dictionary
