#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''
        description: deletes a key from a dictionary if it exist
    '''
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
