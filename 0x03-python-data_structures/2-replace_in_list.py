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

    if idx >= 0 and idx <= list_range:
        my_list[idx] = element
        return my_list
    return my_list
