#!/usr/bin/python3
"""Add attribute"""


def add_attribute(obj, key, value):
    """Adds a new attribute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
