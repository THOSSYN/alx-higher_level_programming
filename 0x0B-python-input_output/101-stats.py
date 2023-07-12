#!/usr/bin/python3
"""Log Parser"""

import sys


def parse_line(line):
    """Parses each line read and call split on them
       to retrieve the status code and file size

       Args:
        line: is the current line read
    """
    segment = line.split()
    if len(segment) >= 2:
        return int(segment[-1]), segment[-2]
    return None, None


def print_result(total_size, status_codes):
    """Prints the result of the stats

       Args:
        total_size (int): the total size for ten lines
        status_codes: is the dictionary of status codes and their counts
    """
    print("File size:", total_size)
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


def get_metric():
    """Determines the status code, file_size and count"""
    status_codes = {}
    total_size = 0

    try:
        for line_number, line in enumerate(sys.stdin, 1):
            file_size, status_code = parse_line(line)
            if file_size is not None and status_code is not None:
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

                if line_number % 10 == 0:
                    print_result(total_size, status_codes)

    except KeyboardInterrupt:
        print_result(total_size, status_codes)


if __name__ == '__main__':
    get_metric()
