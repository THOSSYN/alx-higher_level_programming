#!/usr/bin/python3

def print_square(size):
    """This function prints a square with the character #

       Args:
        size (int): is the sides of the square

       Raise:
        TypeError: if size is not an integer
        TypeError: if size is a float and less than 0
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for value in range(size):
        print('#' * size)
