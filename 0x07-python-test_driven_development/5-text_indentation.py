#!/usr/bin/python3

def text_indentation(text):
    """unction that prints a text with 2 new lines after each
       of these characters: ., ? and :

       Arg:
        text (str):

       Raise:
        TypeError: if text is not string
    """
    char_check = ['.', ',', '?', ':']

    if type(text) != str:
        raise TypeError("text must be a string")

    result = ""
    start_line = True

    for char in text:
        if char == " " and start_line:
            continue
        result += char
        if char in char_check:
            result += "\n\n"
            start_line = True
        else:
            start_line = False

    print(result.rstrip())
