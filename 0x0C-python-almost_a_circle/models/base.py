#!/usr/bin/python3
'''
base class module
'''


class Base():
    '''
    a base class
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if id is None or id < 0:
            self.__class__.__nb_objects += 1
            self.__id = self.__class__.__nb_objects
        else:
            self.__id = id
