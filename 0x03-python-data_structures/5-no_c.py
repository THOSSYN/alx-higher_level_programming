#!/usr/bin/python3
def no_c(my_string):
    """a function that removes all characters c and C
       from a string.

       Args:
        first_arg: my_string

       Return: new_string
    """
    for char in range(len(my_string)):
        if my_string[char] == 'c' or my_string[char] == 'C':
            my_string = my_string[:char] + my_string[char + 1:]
            return (my_string)
