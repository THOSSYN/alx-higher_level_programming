#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """A function that prints all integers of a list
       in reverse order.

       Args:
        first_arg: my_list=[]
    """
    list_range = len(my_list) - 1
    for i in range(list_range, -1, -1):
        print("{}".format(my_list[i]))
