#!/usr/bin/python3
for x in range(97, 123):
    if x % 2 != 0:
        x = chr(x - 32)
    else:
        print(x)
