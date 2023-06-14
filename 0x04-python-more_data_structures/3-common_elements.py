#!/usr/bin/python3
def common_elements(set_1, set_2):
    """a function that returns a set of common
       elements in two sets

       Args:
        first arg: set_1
        second arg: set_2
    """
    return set(set_1 & set_2)
