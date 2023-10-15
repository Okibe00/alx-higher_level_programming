#!/usr/bin/python3
'''
Module creates a square class
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    A square class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        initialiazation method
        '''
        self.size = size
        super().__init__(width=size, height=size, x=x, y=y, id=None)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        '''
        returns the string representation of an object
        '''
        name = self.__class__.__name__
        return f"[{name}] ({self.id}) {self.x}/{self.y} - {self.height}"
