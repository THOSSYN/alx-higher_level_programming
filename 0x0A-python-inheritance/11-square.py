#!/usr/bin/python3
"""Create a Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square"""
    def __init__(self, size):
        """Initializes an instance of size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of Square"""
        return self.__size ** 2

    def __str__(self):
        """Return string representation of area of Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
