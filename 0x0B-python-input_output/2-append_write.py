#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8)
       and returns the number of characters added:

       Args:
        filename: is the name of the file
        text: is the content of the file
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        written = a_file.write(text)
        return written
