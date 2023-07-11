#!/usr/bin/python3
"""Creates a list"""


class MyList(list):
    """Represent MyList"""

    def print_sorted(self):
        """Prints sorted list"""
        result = sorted(self)
        print(result)
