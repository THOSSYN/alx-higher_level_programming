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

    for i in range(list_range):
        if idx < 0 and idx > list_range:
            return (my_list)
        elif idx == i:
            del my_list[i]
            return (my_list)
