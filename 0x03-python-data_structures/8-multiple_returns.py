#!/usr/bin/python3
def multiple_returns(sentence):
    """A function that returns a tuple with the length of
       a string and its first character.

       Args:
        first arg: sentence
    """
    if sentence != "":
        return len(sentence), sentence[0]
    elif sentence == "":
        return len(sentence), None;
