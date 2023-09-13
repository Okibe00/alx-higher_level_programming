#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''
        description: sort dictionary keys
    '''
    for k, v in (dict(sorted((a_dictionary.items()))).items()):
        print(f"{k}: {v}")
