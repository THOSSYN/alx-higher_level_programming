#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """a function that returns a new dictionary
       with all values multiplied by 2

       Args:
        first arg: a_dictionary

       Return: a new dictionary
    """
    new_dic = {}
    for x, y in a_dictionary.items():
        new_dic[x] = y * 2
    return new_dic
