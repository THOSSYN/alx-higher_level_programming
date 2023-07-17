#!/usr/bin/python3
"""Square Class"""

from models.rectangle import Rectangle
"""Import Rectangle class from its package"""


class Square(Rectangle):
    """Represents a class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the class atributes

           Args:
            size (int): Is the size of the square
            x (int): is the x-axis
            y (int): is the y-axia
            id (int): is the identification for each object created
            during instantiation
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size to value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the class Square"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return a string representation of Square"""
        return f"[Square] ({self.id}), {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Returns a dictionary representation of the square object"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
