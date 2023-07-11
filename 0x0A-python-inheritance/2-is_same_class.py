#!/usr/bin/python3
"""Returns True Or False if isinstance"""


def is_same_class(obj, a_class):
    """A function that returns True if the object is
       exactly an instance of the specified class; otherwise False.

       Args:
        obj: is the object
        a_class: is the class

       Return (bool): True if isinstance otherwise false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
