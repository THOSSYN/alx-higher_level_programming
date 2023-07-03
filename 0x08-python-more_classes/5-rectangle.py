#!/usr/bin/python3
"""Creates a Rectangle"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle

           Args:
            width (int): is the widest side
            height (int): is the highest side
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """returns the string representation of a rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(['#' * self.width] * self.height)

    def __repr__(self):
        """returns the string representation"""
        return f"Rectangle(width={self.width}, height={self.height})"

    def __del__(self):
        """detect the deletion of a string"""
        print("Bye rectangle...")
