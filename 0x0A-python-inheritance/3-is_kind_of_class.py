#!/usr/bin/python3
'''
module checks for instances
'''


def is_kind_of_class(obj, a_class):
    '''
    checks if a class is an instance of an obj
    Args:
        obj: object
        a_class: class
    Return: True or False
    '''
    return (isinstance(obj, a_class))
