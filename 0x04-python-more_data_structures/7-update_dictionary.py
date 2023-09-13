#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    '''
        description: Replaces or adds key/value in a dictionary
    '''
    if key not in a_dictionary:
        a_dictionary.update({key: value})
    else:
        a_dictionary[key] = value
    return a_dictionary
