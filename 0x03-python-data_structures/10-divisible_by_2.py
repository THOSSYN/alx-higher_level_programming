#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """a function that finds all multiples of 2 in a list.
       
       Args:
        first arg: my_list

       Return: Return a new list with True or False
    """
   # my_newlist = my_list.copy()
    res = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            res.append(True)
        else:
            res.append(False)
        return res
