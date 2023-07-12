#!/usr/bin/python3
"""Class to json"""

MyClass = __import__('8-my_class').MyClass


def class_to_json(obj):
    """A function that returns the dictionary description of
       with simple data structure

       Args:
        obj: is the python object
    """
    if isinstance(obj, MyClass):
        return {'name': obj.name,
                'number': obj.number}
    else:
        raise TypeError("Object is not serializable")
