#!/usr/bin/python3
def no_c(my_string):
    """a function that removes all characters c and C
       from a string.

       Args:
        first_arg: my_string

       Return: new_string
    """
    new_str = ""

    for char in my_string:
        if char != 'c' and char != 'C':
            new_str += char
    return new_str
