#!/usr/bin/python3
for chars in range(97, 123):
    if chars == 113 or chars == 101:
        continue
    print(chr(chars), end="")
