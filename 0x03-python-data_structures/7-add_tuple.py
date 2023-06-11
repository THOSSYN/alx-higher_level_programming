#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """A function that adds 2 tuples.
        
       Args:
        first arg: tuple_a
        second_arg: tuple_b

       Return: a tupple with two integers
    """
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (result)
