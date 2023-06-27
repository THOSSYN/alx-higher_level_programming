#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Represents a square class"""

    def __init__(self, size=0):
        """Initializes a new square instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of a square."""
        return self.__size ** 2
