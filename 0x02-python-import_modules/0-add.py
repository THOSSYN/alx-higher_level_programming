#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    """0-add.py add two variable a and b by importing add-0
    Arguments:
        a: first parameter
        b: second parameter

    Returns:
        The value a + b
    """
    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))
