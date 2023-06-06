#!/usr/bin/python3
def uppercase(string):
    for x in string:
        if x >= 'a' and x <= 'z':
            x = chr(ord(x) - 32)
        print(x, end = "")
    print("")
