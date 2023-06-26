#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except ZeroDivisionError:
        result = None
        sys.stderr.write("Exception: division by zero\n")
        return None
    except IndexError:
        sys.stderr.write("Exception: list index out of range\n")
        return None
