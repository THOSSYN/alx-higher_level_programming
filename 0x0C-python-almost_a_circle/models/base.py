#!/usr/bin/python3
"""Base class"""

import json
import csv
import turtle


class Base:
    """Represents a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a class attribute id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

           Args:
            list_dictionaries: is a python dictionary object
        """
        if list_dictionaries is None:
            return "[]"
        else:
            json_data = json.dumps(list_dictionaries)
            return json_data

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])

        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

           Args:
            json_string:
        """
        if json_string is None and len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

           Args:
            dictionary: is a dictionary of attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as f:
                json_data = f.read()
        except FileNotFoundError:
            return []
        if json_data == "":
            return []
        dictionary = cls.from_json_string(json_data)
        instances = [cls.create(**inst) for inst in dictionary]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv file

           Args:
            list_objs: is the variable holding the content of list
        """
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline="") as f:
            csv_writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    csv_writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes csv data"""
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                instance = []
                for row in csv_reader:
                    if cls.__name__ == "Rectangle":
                        id, width, height, x, y = map(int, row)
                        new = cls.create(
                                id=id, width=width, height=height, x=x, y=y)
                        instance.append(new)
                    elif cls.__name__ == "Square":
                        id, size, x, y = map(int, row)
                        new = cls.create(id=id, size=size, x=x, y=y)
                        instance.append(new)
                return instance
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares

           Args:
            list_rectangles: a list of rectangle attributes
            list_squares: a list of square attributes
        """
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.setup(800, 600)

        pen = turtle.Turtle()

        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        pen.hideturtle()

        turtle.done()
