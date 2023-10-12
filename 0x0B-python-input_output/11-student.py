#!/usr/bin/python3
'''
module to write to a file
'''


class Student:
    '''
    student class
    '''
    def __init__(self, first_name, last_name, age):
        '''
            init method
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        '''
            returns obj dictionary
        '''
        if type(attr) == list:
            return {t: self.__dict__[t] for t in attr if t in self.__dict__}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        self.__dict__.update(json)
