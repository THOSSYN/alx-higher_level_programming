#!/usr/bin/python3
#4-print_hexa.py

"""Prints all numbers from 0 to 98 in decimal and
in hexadecimal"""
i = 0

while i <= 98:
    print("{:d} = {:x}".format(i, i))
    i += 1
