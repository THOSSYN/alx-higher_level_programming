#!/usr/bin/python3
num = 0
while num <= 99:
    if num < 10:
        print(F"0{num:d}", end=", ")
    elif num > 10:
        if num == 99:
            print(num)
            break
        else:
            print(F"{num:d}", end=", ")
    num += 1
