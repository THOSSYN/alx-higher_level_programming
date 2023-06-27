#!/usr/bin/python3
class Square:
    """
    This class represents a square.

    Attribute:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square object
    """
    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square

        Raises:
            TypeError: if the size is not an integer.
            ValueError: If rhe size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
