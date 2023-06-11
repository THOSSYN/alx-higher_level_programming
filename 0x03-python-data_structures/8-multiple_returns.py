#!/usr/bin/python3
def multiple_returns(sentence):
    """A function that returns a tuple with the length of
       a string and its first character.

       Args:
        first arg: sentence
       
    """
    count = 0
    for i in range(len(sentence)):
        count += 1
    return (count), (sentence[0])
