#!/usr/bin/python3
# 2-square.py
"""defines a class called square"""


class Square:
    """defines and initializes using __init__"""
    def __init__(self, size=0):
        """handle errors"""
        """check if size is not int"""
        if type(size) is not int:
            """prints out TypeError exception"""
            raise TypeError("size must be an integer")
        """check if size is less than zero"""
        elif size < 0:
            """
            raise a ValueError exception because
            minimum value should be zero
            """
            raise ValueError("size must be >= 0")
        """assigns value to an object"""
        self.__size = size
