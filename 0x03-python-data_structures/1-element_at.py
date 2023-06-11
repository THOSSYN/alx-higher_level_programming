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
    for num in range(list_range):
        if idx < 0:
            return (None)
        elif idx > list_range:
            return (None)
        elif idx == num:
            return (my_list[num])
