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
    def load_from_file(cls):
        '''
        returns a list of instances
        '''
        file_name = cls.__name__+'.json'
        try:
            with open(file_name, 'r', encoding='utf-8') as fd:
                string = fd.read()
                list_obj = cls.from_json_string(string)
                list_inst = list()
                for obj in list_obj:
                    list_inst.append(cls.create(**obj))
                return list_inst
        except Exception:
            return []

    @classmethod
    def create(cls, **dictionary):
        '''
         creates a new class
        '''
        if cls.__name__ == 'Rectangle':
            inst = cls(2, 2)
            inst.update(**dictionary)
        if cls.__name__ == 'Square':
            inst = cls(2)
            inst.update(**dictionary)
        return inst

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        save json to file
        '''
        cls_name = cls.__name__ + '.json'
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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_str = json.dumps(list_dictionaries)
            return json_str

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
