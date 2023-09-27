#!/usr/bin/python3
'''Square.
This module creates a  square class.
'''


class Square:
    '''A simple class of a sqaure
    attribute:
        __size (int): private varible size
    '''
    def __init__(self, size=0):
        '''Initializes an instance of the class
        Args x: size of square
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
