#!/usr/bin/python3
"""Creates a Rectangle"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance

           Args:
            width (int): widest side of rectangle
            height (int): highest side of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width property

           Args:
            value (int): is the value set for width

           Raise:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height property

           Args:
            value (int): is the value set for height

           Raise:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """returns a string representation of rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(['#' * self.width] * self.height)

    def __repr__(self):
        """returns a string representation of rectangle"""
        return f"Rectangle({self.width}, {self.height})"
