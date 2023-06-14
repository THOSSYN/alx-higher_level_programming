#!/usr/bin/python3
def best_score(a_dictionary):
    """a function that returns a key with the
       biggest integer value.

       Args:
        first arg: a_dictionary

       Return: None if no score is found or the
               key/value pair of the highest value
    """
    if a_dictionary:
        for x, y in a_dictionary.items():
            if y == max(a_dictionary.values()):
                return x
    return None
