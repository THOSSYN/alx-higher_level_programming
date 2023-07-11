#!/usr/bin/python3
"""A MyInt class that inherits from int"""


class MyInt(int):
    """Represents MyInt class"""
    def __init__(self, value):
        """Initializes an instance of value"""
        self.value = value

    def __eq__(self, other):
        """Compare the equality of two number but inverted"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Compares the non-equality of two number but inverted"""
        return super().__eq__(other)
