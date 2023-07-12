#!/usr/bin/python3
"""Search and Update"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file, after each
       line containing a specific string

       Args:
        filename: is the file to be opened for searching
        search_string: is the string being searched for
        new_string: is the string to be appended after the line
        where the search_string occur
    """
    line_list = []

    with open(filename, mode='r+', encoding='utf-8') as sf:
        read = sf.readlines()
        for line in read:
            line_list.append(line)
            if search_string.lower() in line.lower():
                line_list.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as sf:
        sf.write(''.join(line_list))
