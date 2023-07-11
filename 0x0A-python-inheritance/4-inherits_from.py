#!/usr/bin/python3
"""Subclass of a class"""


def inherits_from(obj, a_class):
    """A function that return true or false if an object inherits
       or not from a class

       Args:
        obj: is the object
        a-class: is the class

       Return (bool): True or False
    """
    return issubclass(type(obj), a_class)
