#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """
        Initializes the square object instance.

        Args:
            size: The size of square
        """
        self.size = size

    @property
    def size(self):
        """Get the value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Compare and return the result"""
        return self.size

    def __eq__(self, other):
        """The equality comparator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """The not equal to comparator"""
        return self.area() != other.area()

    def __gt__(self, other):
        """The greater than comparator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """The greater than or equal to"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """The less than comparator"""
        return self.area() < other.area()

    def __le__(self, other):
        """The less than or equal to comparator"""
        return self.area() <= other.area()
