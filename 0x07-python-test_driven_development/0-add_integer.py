#!/usr/bin/python3

def add_integer(a, b=98):
    """This function add two integers
    
       Args:
        a (int)(float): is the first argument to be passed
        b (int)(float): 98 (default value) second argument to be
                 if no argument is passed

       Return (int): the addition of a and b
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = int(a) + int(b)
        return int(result)
    elif not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    else:
        raise TypeError("b must be an integer")
