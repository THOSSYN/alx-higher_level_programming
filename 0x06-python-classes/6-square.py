#!/usr/bin/python3
"""Defines a Square object"""


class Square:
    """Represents a Square Object"""

    def __init__(self, size=0, position=(0, 0)):
        """
        initializes an object instance.

        Args:
            size (int): The size of the square
            position int(tuple): being position retrieved from squae
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the value from the setter"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is the setter

        Args:
            value (int): Is the value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the value from the setter"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        This is the setter

        Args:
            value (int): Is the value to set
        """
        if not isinstance(value, tuple) or len(value) != 2\
                or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints square with # character to stdout"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
