#!/usr/bin/python3
"""Creates a Rectangle"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the Rectangle instance

           Arg:
            width (int): one side of the rectangle
            height (int): the other side of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method. Set value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method. Set value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
