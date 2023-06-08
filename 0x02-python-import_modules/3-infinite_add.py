#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv)
    if arg_count == 1:
        print("{:d}".format(0))
    if arg_count == 2:
        print("{}".format(int(sys.argv[1])))
    if arg_count > 2:
        total = 0
        for args in range(1, arg_count):
            total += int(sys.argv[args])
        print("{}".format(total))
