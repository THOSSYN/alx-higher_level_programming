#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """Creates the class Square object"""

    def __init__(self, size=0):
        """
        Initializes the Square size

        Args:
            size (int): The size of the Square object
        """
        self.size = size

    @property
    def size(self):
        """This is the getter method
        It gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets value to attribute

        Args:
            Value: value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of square"""
        return self.__size ** 2
