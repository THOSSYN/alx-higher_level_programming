#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """A function that prints all integers of a list
       in reverse order.

       Args:
        first_arg: my_list=[]
    """
    if my_list is not None:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
