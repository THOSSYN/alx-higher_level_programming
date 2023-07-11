#!/usr/bin/python3
"""Defines an object attribute for lookup function"""


def lookup(obj):
    """A function that returns a list of
       attribute of an object

       Args:
        obj (str): is the instance
    """
    return dir(obj)
