#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """A function that replaces an element in a list at a
       specific position without modifying the original list
    """
    list_copy = my_list.copy()
    list_range = len(list_copy)

    for i in range(list_range):
        if idx < 0:
            return (list_copy)
        elif idx > list_range:
            return (list_copy)
        elif idx == i:
            list_copy[i] = element
            return (list_copy)
