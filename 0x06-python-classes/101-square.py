#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the value size"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value"""
        if not isinstance(value, tuple) or len(value) != 2\
                or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints the area with # character"""
        if self.__size == 0:
            print(" ")
        else:
            for _ in range(self.__position[1]):
                print(" ")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the string to be displayed"""
        sq_str = ""
        if self.__size == 0:
            return sq_str
        else:
            for _ in range(self.__position[1]):
                sq_str += "\n"
            for _ in range(self.__size):
                sq_str += " " * self.__position[0] + "#" * self.__size + "\n"
            return sq_str
