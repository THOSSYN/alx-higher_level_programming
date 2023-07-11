#!/usr/bin/python3
"""Creates a square that inherits from 9-rectangle.py"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square"""
    def __init__(self, size):
        """Initializes an instance of size"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """returns area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of area"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
