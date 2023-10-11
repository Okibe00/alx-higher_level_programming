#!/usr/bin/python3

'''
modules creates a class
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    rectangle class
    '''
    def __init__(self, width, height):
        '''
        initializes Rectangle
        '''
        self.__width = width
        self.__height = height
