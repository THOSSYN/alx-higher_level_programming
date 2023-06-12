#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """A function that deletes items at a specific
       position in a list.

       Args:
        first arg: my_list
        second arg: idx

       Return: my_list if idx is negative or out of range.
    """
    list_range = len(my_list) - 1

    if idx >= 0 and idx <= list_range:
        del my_list[idx]
        return my_list
    return my_list
