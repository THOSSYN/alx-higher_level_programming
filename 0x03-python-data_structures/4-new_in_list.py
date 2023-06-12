#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """A function that replaces an element in a list at a
       specific position without modifying the original list
    """
    list_copy = my_list.copy()
    list_range = len(list_copy) - 1

    if idx >= 0 and idx <= list_range:
        list_copy[idx] = element
        return (list_copy)
    return list_copy
