#!/usr/bin/python3
'''
module checks for instances
'''


def inherits_from(obj, a_class):
    '''
    checks if a class is an instance of an obj
    Args:
        obj: object
        a_class: class
    Return: True or False
    '''
    if isinstance(obj, a_class) and issubclass(obj.__class__, a_class):
        return True
    else:
        return False
