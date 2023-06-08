#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv) - 1
    if arg_count == 0:
        print("{} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{} argument:".format(arg_count))
    else:
        print("{} arguments:".format(arg_count))
    for args in range(arg_count):
        print("{}: {}".format(args + 1, sys.argv[args + 1]))
