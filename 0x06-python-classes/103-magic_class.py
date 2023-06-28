#!/usr/bin/python3
import math


"""A Python class that does what a ByteCode do"""


class Radius:
    """"""
    def __init__(self, radius=0):
        """
        Initializes an instance of the class"""
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Returns area of a circle"""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Return the circumference of a circle"""
        return 2 * math.pi * self.__radius
