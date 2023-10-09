#!/usr/bin/python3
'''
module that gets arrtibute of an object
'''


def lookup(obj):
    '''
       Returns the list of attributes and methods in an obj
       Args:
            obj: only argument
       Return:
            obj attributes and methods
    '''
    return (list(dir(obj)))
