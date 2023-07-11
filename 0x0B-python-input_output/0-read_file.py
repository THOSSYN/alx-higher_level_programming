#!/usr/bin/python3
"""File Reading"""


def read_file(filename=""):
    """A function that reads a text file (UTF-8) and
       prints it to stdout

       Args:
        Filename: is the name of the file
    """
    with open(filename, encoding='UTF-8') as a_file:
        print(a_file.read())
