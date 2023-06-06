#!/usr/bin/python3
#6-print_comb3.py

"""Prints all possible different combination
of two digits."""
for outer in range(0, 10):
    for inner in range(outer + 1, 10):
        if outer == 8 and inner == 9:
            print("{}{}".format(outer, inner))
        else:
            print("{}{}".format(outer, inner), end=", ")
