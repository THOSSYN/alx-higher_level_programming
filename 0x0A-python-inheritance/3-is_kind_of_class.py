#!/usr/bin/python3
"""Verifies if same class or not"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if object
       is an instance or False

       Args:
        obj: is the object
        a_class: is the class

       Return (bool): True or False
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
