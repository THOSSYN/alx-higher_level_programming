#!/usr/bin/python3
#100-print_tebahpla.py

"""Prints alphabets in reverse alternating
uppercase and lowercase"""
i = 0
for x in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(x - i)), end="")
    if i == 0:
        i = 32
    else:
        i = 0
