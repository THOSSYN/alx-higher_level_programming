#!/usr/bin/python3
"""Class to json"""


def class_to_json(obj):
    """A function that returns the dictionary description of
       with simple data structure

       Args:
        obj: is the python object
    
    if isinstance(obj, MyClass):
        return {'name': obj.name,
                'number': obj.number}
    else:
        raise TypeError("Object is not serializable")
    """
    def class_to_json(obj):
    """A function that returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: The Python object to be serialized.
    """
    if not isinstance(obj, type):  # Check if obj is an instance of a Class
        raise TypeError("Object is not an instance of a Class")

    attributes = {}

    for attr_name in dir(obj):  # Loop through all attributes of the object
        if not attr_name.startswith("__"):  # Exclude dunder attributes
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):  # Check if attribute is serializable
                attributes[attr_name] = attr_value

    return attributes
