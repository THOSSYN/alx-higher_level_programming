#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """A function that replaces all occurences of an
       element by another in a new list

       Args:
        first arg: my_list
        second arg: search
        third arg: replace
    """
    new_list = []
    for num in my_list:
        if num != search:
            new_list.append(num)
        else:
            new_list.append(replace)
    return new_list
