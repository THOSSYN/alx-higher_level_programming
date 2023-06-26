#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """a function that divides element by element 2 lists.

       Args:
        first arg: my_list_1
        second arg: my_list_2

       Return: a new list
    """
    result = []
    try:
        for i in range(list_length):
            try:
                if (isinstance(my_list_1[i], (int, float)) and
                        isinstance(my_list_2[i], (int, float))):
                    result.append(my_list_1[i] / my_list_2[i])
                else:
                    result.append(0)
                    print("wrong type")
            except ZeroDivisionError:
                result.append(0)
                print("division by 0")
            except IndexError:
                result.append(0)
                print("out of range")
    finally:
        return result
