#!/usr/bin/python3
"""Defines a Square object"""


class Square:
    """Create a Square Object"""

    def __init__(self, size=0):
        """
        Initializes a Square object instance

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """It retrieves value"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints square to stdout with # character"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
