#!/usr/bin/python3
def weight_average(my_list=[]):
    """a function that returns the weighted average
       of all integers tuple (<score>, <weight>)

       Args:
        first arg: my_list

       Return: 0 if the list is empty
    """
    if not my_list:
        return 0
    total_weight = 0
    weighted_sum = 0

    for x, y in my_list:
        total_weight += y
        weighted_sum += x * y

    return weighted_sum / total_weight
