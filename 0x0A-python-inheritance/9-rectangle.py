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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        '''
        prints string representation of object
        '''
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"

    def area(self):
        '''
        gets area of rectangle
        '''
        return self.__width * self.__height
