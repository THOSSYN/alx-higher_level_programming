#!/usr/bin/python3

def lookup(obj):
    """A function that returns a list of
       attribute of an object

       Args:
        obj (str): is the instance
    """
    return dir(obj)
