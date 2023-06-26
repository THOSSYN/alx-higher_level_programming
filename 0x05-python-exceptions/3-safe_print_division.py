#!/usr/bin/python3
def safe_print_division(a, b):
    """A function that divides two interger and prints
       the result

       Args:
        first arg: a
        second arg: b

       Return: the value of the division or None
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
