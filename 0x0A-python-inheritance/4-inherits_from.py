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
    obj_cls = obj.__class__
    if issubclass(obj_cls.__base__, a_class):
        return True
    else:
        return False
