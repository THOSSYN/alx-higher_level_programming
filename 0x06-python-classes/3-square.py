#!/usr/bin/python3
# 3-square.py

class Square:
    """
    Iniatializes a Square object

    Attribute:
        __size (int): The size of the square

    Methods:
        __init__(self, size=0): Initializes a Square object
        area(self): returns the area of the square
    """
    def __init__(self, size=0):
        """
        Iniatializes a Square object

        Args:
            size (int): The size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of a square.

        Return:
            int: The current square area.
        """
        return self.__size ** 2
