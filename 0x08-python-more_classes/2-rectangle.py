#!/usr/bin/python3
"""Creates a Rectangle"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes an instance of Rectangle

           Args:
            width (int): is the widest side of the Rectangle
            height (int): is the highest side of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the value that is being set"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value for the getter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the value that is being set"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value for the getter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of a Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
