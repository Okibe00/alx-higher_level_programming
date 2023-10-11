#!/usr/bin/python3
'''
module to write to a file
'''
import json


def from_json_string(my_str):
    '''
    converts a json string to obj
    '''
    return (json.loads(my_str))
