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
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def to_dictionary(self):
        '''
        returns dictionary representation of square
        '''
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}

    def update(self, *args, **kwargs):
        '''
        update class attributes
        '''
        if args is not None and len(args) != 0:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = self.integer_validator("id", v)
                elif i == 1:
                    self.width = v
                    self.height = v
                elif i == 2:
                    self.x = v
                elif i == 3:
                    self.y = v
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = self.integer_validator("id", v)
                elif k == "size":
                    self.width = v
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    @property
    def size(self):
        '''
        gets the size of the square
        '''
        return self.width

    @size.setter
    def size(self, size):
        '''
        sets the size of the square
        '''
        self.width = size
        self.height = size

    def __str__(self):
        '''
        returns the string representation of an object
        '''
        name = self.__class__.__name__
        return f"[{name}] ({self.id}) {self.x}/{self.y} - {self.height}"
