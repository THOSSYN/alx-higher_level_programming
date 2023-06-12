#!/usr/bin/python3
def element_at(my_list, idx):
    """A function that retrieves an element from
       a list like in C

       Args:
        first arg: my_list
        second arg: idx

       Return: None
    """
    list_range = len(my_list) - 1
    if idx >= 0 and idx <= list_range:
        return my_list[idx]
    return None
