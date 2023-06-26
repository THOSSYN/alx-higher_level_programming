#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list

       Args:
        first arg: my_list
        second arg: x

       Return: the real number of elements printed
    """
    try:
        count = 0
        for i in my_list:
            if count < x:
                print(i, end="")
                count += 1
            else:
                break
        print()
    except:
        pass
    return count
