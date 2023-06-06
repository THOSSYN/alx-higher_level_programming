#!/usr/bin/python3
#3-print_alphabt.py

"""Prints the ASCII alphabets in lowercase
not followed by a new line"""
for chars in range(97, 123):
    if chars == 113 or chars == 101:
        continue
    print("{}".format(chr(chars)), end="")
