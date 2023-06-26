#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    """a function that prints an integer.

       Args:
        first arg: value

       Return: True if value has been correctly printed
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        sys.stderr.write("Exception: Unknown format code 'd' for object of type 'str'\n")
        return False
