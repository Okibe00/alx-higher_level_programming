#!/usr/bin/python3
'''
module checks for instances
'''


def is_same_class(obj, a_class):
    '''
    checks if a class is an instance of an obj
    Args:
        obj: object
        a_class: class
    Return: True or False
    '''
    if (type(obj) is a_class):
        return True
    else:
        return False
