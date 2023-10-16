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

    @classmethod
    def create(cls, **dictionary):
        inst = cls(2, 2, 2, 2)
        inst.update(**dictionary)
        return inst

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        save json to file
        '''
        cls_name = cls.__base__ + '.json'
        list_dic = list()

        if isinstance(list_objs, list):
            for i in list_objs:
                list_dic.append(i.to_dictionary())

        string = cls.to_json_string(list_dic)
        with open(cls_name, 'w', encoding="utf-8") as fd:
            fd.write(string)

    def from_json_string(json_string):
        '''
        return list of string representaion\
        of json_string
        '''
        if json_string is not None:
            return json.loads(json_string)
        else:
            return []

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
