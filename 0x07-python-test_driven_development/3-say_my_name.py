#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """This function prints My name is <first name> <last name>

       Args:
        first_name (string): is the first name
        last_name (string): is the last name

       Raise:
        TypeError: if last name and first_name are not string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string or last_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string or last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
