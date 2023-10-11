#!/usr/bin/python3

'''
modules creates a class
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
        creates a square
    '''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''
            returns the area of a square
        '''
        return self.__size ** 2

    def __str__(self):
        '''
        returns string representatio
        '''
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
