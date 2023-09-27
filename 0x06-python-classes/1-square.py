#!/usr/bin/python3
'''Square.
This module creates a  square class.
'''


class Square:
    '''A simple class of a sqaure
    attribute:
        __size (int): private varible size
    '''
    def __init__(self, x):
        '''Initializes an instance of the class
        Args x: size of square
        '''
        self.__size = x
