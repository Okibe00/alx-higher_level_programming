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
        self.__size = size

    @property
    def size(self):
        '''gets the value of square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''get the size of the square
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
