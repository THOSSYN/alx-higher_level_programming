#!/usr/bin/python3
"""Class to json"""


def class_to_json(obj):
    """A function that returns the dictionary description of
       with simple data structure

       Args:
        obj: is the python object
    """
    if not isinstance(obj, type):  # Check if obj is an instance of a Class
        raise TypeError("Object is not an instance of a Class")

    attributes = {}

    for attr_name in dir(obj):
        if not attr_name.startswith("__"):
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                attributes[attr_name] = attr_value

    return attributes
