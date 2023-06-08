#!/usr/bin/python3
def magic_calculation(a, b):
    """A function that does exactly the same as a
        given bytecode

        Arguments:
            arg1: a
            arg2: b

        Return: the addition of a and b if a is less than b
        else it return the difference of a and b
    """
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return (sub(a, b))
