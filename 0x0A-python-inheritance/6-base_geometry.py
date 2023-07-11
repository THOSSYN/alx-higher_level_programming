#!/usr/bin/python3
"""Creates a BaseGeometry"""


class BaseGeometry:
    """Represents a BaseGeometry"""

    def area(self):
        """Raise a NotImplementedError"""
        raise Exception("area() is not implemented")
