#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """A function that prints the first x elements of a list
       and only integers.

    Args:
        my_list: The list to print elements from (default is an empty list)
        x: The number of elements to print (default is 0)

    Returns:
        The real number of integers printed
    """
    num_count = 0
    try:
        for i in my_list:
            if num_count < x:
                if isinstance(i, int):
                    num_count += 1
                    print("{:d}".format(i), end="")
            else:
                break
        print()
    except Exception:
        pass
    return num_count
