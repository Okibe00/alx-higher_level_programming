#!/usr/bin/python3
'''
module to write to a file
'''
import json


def to_json_string(my_obj):
    '''
    converts an object into a json string
    '''
    return (json.dumps(my_obj))
