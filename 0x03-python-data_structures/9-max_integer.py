#!/usr/bin/python3
def max_integer(my_list=[]):
    """A function that finds the biggest integer
       of a list

       Args:
        first arg: my_list

       Return: the max integer or None if lis is empty
    """
    if my_list == []:
        return (None)

    i = len(my_list) - 1

    while i > 1:
        j = 0
        while j < i:
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
            j += 1
        i -= 1
    return my_list[len(my_list) - 1]
