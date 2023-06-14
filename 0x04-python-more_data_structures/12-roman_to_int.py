#!/usr/bin/python3
def roman_to_int(roman_string):
    """A function that converts a Roman Numeral
       to an integer

       Args:
        first arg: roman_string

       Return: 0 if roman_string is None
    """
    if roman_string:
        roman_dict = {
                'I': 1,
                'IV': 4,
                'V': 5,
                'IX': 9,
                'X': 10,
                'XL': 40,
                'L': 50,
                'C': 100,
                'CD': 400,
                'D': 500,
                'CM': 900,
                'M': 1000
                }
        total = 0
        for x, y in roman_dict.items():
            for char in roman_string:
                if char == x:
                    total += y
        return total
    return 0
