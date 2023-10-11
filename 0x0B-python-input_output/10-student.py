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
            return {k: self.__dict__[k] for k in attr if k in self.__dict__}
        else:
            return self.__dict__
