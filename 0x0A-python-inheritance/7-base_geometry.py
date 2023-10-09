#!/usr/bin/python3
'''
modules creates a class
'''


class BaseGeometry:
    '''
    base geometry class
    '''

    def area(self):
        '''
            raises an exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
            validates value
        '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
