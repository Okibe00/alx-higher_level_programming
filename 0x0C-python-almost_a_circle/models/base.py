#!/usr/bin/python3
'''
base class module
'''

import json


class Base():
    '''
    a base class
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        converts object to json
        '''
        if isinstance(list_dictionaries, list) and len(list_dictionaries) != 0:
            json_str = json.dumps(list_dictionaries)
            return json_str
        else:
            return "[]"

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
