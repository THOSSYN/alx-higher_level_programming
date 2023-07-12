#!/usr/bin/python3
"""Class to json"""

MyClass = __import__('8-my_class').MyClass
MyClass = __import__('8-my_class_2').MyClass

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
    obj_class = type(obj)
    if obj_class.__module__ == '__main__':
        class_name = obj_class.__name__
    else:
        class_name = obj_class.__module__ + '.' + obj_class.__name__

    if isinstance(obj, (list, dict, str, int, bool)):
        return obj
    elif isinstance(obj, MyClass) or isinstance(obj, MyClass2):
        return {
            '__class__': class_name,
            **obj.__dict__
        }
    else:
        raise TypeError("Object is not serializable")
