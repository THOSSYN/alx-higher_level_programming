#!/usr/bin/python3
def safe_print_integer(value):
    """A function that prints an integer with "{:d}".format().

       Args:
        first arg: value

       Return: True or False
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
