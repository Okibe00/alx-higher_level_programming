#!/usr/bin/python3
def best_score(a_dictionary):
    '''
        description: returns the key with largest value
    '''
    key = None
    value = 0
    if a_dictionary is None:
        return None
    for k, v in a_dictionary.items():
        if key is None:
            key = k
            value = v
        else:
            if v > value:
                key = k
                value = v
    return key
