#!/usr/bin/python3
"""Creates a LockedClass"""


class LockedClass:
    """Represent a LockedClass"""
    __slot__ = ['first_name']

    def __setattr__(self, name, value):
        """Set name attribute only if first_name

           Args:
            name: is name field to be set
            value: is the name given
        """
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute\
 'last_name'")
        else:
            self.__dict__[name] = value
