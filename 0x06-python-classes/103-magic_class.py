#!/usr/bin/python3
"""A Python class that does what a ByteCode do"""

import math


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius=0):
        """
        Initializes an instance of the class

        Args:
            radius (int): The radius of the class
        """
        self.radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns area of a circle"""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Return the circumference of a circle"""
        return 2 * math.pi * self.__radius
