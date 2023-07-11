#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
       and returns the number of characters written:

       Args:
        filename: is the name of the file
        text: is the content of the file
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        written = a_file.write(text)
        return written
