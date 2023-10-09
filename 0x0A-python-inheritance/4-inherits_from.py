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
    lx = obj.__class__
    while lx is not None:
        if lx == a_class:
            return True
        lx = lx.__base__
