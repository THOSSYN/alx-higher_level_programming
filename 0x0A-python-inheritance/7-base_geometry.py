#!/usr/bin/python3
"""Integer Validator"""


class BaseGeometry:
    """Represents a BaseGeometry"""

    def area(self):
        """Area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value of an integer

           Args:
            name (str): is the name of the parameter
            value (int): is the value of name
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
