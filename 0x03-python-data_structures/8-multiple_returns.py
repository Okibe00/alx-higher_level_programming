#!/usr/bin/python3
def multiple_returns(sentence):
    '''
        description: returns a tupel with length of string
        and its first character
    '''
    len_str = len(sentence)
    if len_str == 0:
        new_tup = len_str, None
        return new_tup
    else:
        new_tup = len_str, sentence[0]
        return new_tup
