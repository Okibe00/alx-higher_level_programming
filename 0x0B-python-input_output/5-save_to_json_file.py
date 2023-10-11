#!/usr/bin/python3
'''
module to write to a file
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    writes json to a file
    '''
    with open(filename, 'w', encoding="utf-8") as fd:
        json.dump(my_obj, fd)
