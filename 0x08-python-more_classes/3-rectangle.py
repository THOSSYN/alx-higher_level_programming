#!/usr/bin/python3
"""Creates a Rectangle"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the Rectangle instance

           Args:
            width (int): is the widest side
            height (int): is the longest side
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the width attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Return the string # to print a rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(['#' * self.width] * self.height)
