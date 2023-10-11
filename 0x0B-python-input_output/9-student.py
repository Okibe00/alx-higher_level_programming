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

    def to_json(self):
        '''
            returns obj dictionary
        '''
        return self.__dict__
