#!/usr/bin/python3
def uniq_add(my_list=[]):
    """a function that adds all unique integers
       in a list (only once for each integer).

       Args:
        first arg: my_list
    """
    total = 0
    for num in set(my_list):
        total += num
    return total
