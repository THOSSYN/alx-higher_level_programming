#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """A function that replaces an element of a list
       a specific position.

       Argumment:
        first_arg: my_list
        second_arg: idx
        third_arg: element

       Return: the original list
    """
    list_range = len(my_list) - 1
    for i in range(list_range):
        if idx < 0:
            return (my_list)
        elif idx > list_range:
            return (my_list)
        elif idx == i:
            my_list[i] = element
            return(my_list)
