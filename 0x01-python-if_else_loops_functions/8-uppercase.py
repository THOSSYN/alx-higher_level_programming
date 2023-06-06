#!/usr/bin/python3
#8-uppercase.py

def uppercase(string):
    """Prints a string in uppercase."""
    for x in string:
        if x >= 'a' and x <= 'z':
            x = chr(ord(x) - 32)
        print(x, end = "")
    print("")
