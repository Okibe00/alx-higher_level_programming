#!/usr/bin/python3
'''modules creates a class'''


class Rectangle:
    '''creates an empty class'''
    def __init__(self, width=0, height=0):
        '''
        initilizes instance of class
        args:
            width: width
            height: height
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
            gets value of width
        '''
        return self.__width

    @width.setter
    def width(self, width):
        '''
        sets value of width
        args:
            width: width value
        '''
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        '''
        gets value of height
        '''
        return self.__height

    @height.setter
    def height(self, height):
        '''
        sets value of height
        args:
            height: height value
        '''
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
