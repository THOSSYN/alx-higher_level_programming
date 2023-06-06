#!/usr/bin/python3
outer = 0
while outer < 8:
    inner = 1
    while inner <= 9:
        print(f"{outer}{inner}", end = ", ")
        inner += 1
    outer += 1
