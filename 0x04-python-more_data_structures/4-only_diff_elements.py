#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """a function that returns a set of all
       elements present in only one set.

       Args:
        first arg: set_1
        second arg: set_2
    """
    return set(set_1 ^ set_2)
