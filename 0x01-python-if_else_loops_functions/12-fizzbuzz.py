#!/usr/bin/python3
#12-fizzbuzz.py

def fizzbuzz():
    """Prints Fizz, Buzz for the numbers from 1 to 100
    seperated by a space"""
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0 and x % 15 == 0:
            print("FizzBuzz", end = " ")
        elif x % 3 == 0:
            print("Fizz", end = " ")
        elif x % 5 == 0:
            print("Buzz", end = " ")
        else:
            print(x, end = " ")
