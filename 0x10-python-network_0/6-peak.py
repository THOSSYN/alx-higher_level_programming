#!/usr/bin/python3

def find_peak(list_of_integers):
    """Finds the peak of a list"""
    if not list_of_integers:
        return None

    length = len(list_of_integers) - 1
    mid = len(list_of_integers) // 2

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        result = list_of_integers[:mid]
    elif mid < length and list_of_integers[mid] < list_of_integers[mid + 1]:
        result = find_peak(list_of_integers[mid + 1:])
    else:
        result = list_of_integers[mid]

    if isinstance(result, list) and len(result) == 1:
        result = result[0]

    return result
