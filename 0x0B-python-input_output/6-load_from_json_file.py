#!/usr/bin/python3
'''
module to write to a file
'''
import json


def load_from_json_file(filename):
    '''
    writes json to a file
    '''
    with open(filename, encoding="utf-8") as fd:
        return json.loads(fd.read())
