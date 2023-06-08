#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    import sys

    arg_count = len(sys.argv) - 1
    if arg_count != 3:
        print("Usage: {} a <operator> b".format(sys.argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sign = sys.argv[2]

    if sign == '+':
        result = cal.add(a, b)
    elif sign =='-':
        result = cal.sub(a, b)
    elif sign == '*':
        result = cal.mul(a, b)
    elif sign == '/':
        result = cal.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, sign, b, result))
