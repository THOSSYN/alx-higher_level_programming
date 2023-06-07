#!/usr/bin/python3
# 5-print_comb2.py

"""Prints numbers from 0 to 99.Numbers must be
separated by , followed by a space"""
for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02d}".format(num), end=", ")
