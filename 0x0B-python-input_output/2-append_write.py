#!/usr/bin/python3
'''
module to write to a file
'''


def append_write(filename="", text=""):
    '''
    writes to a file
    '''
    with open(filename, 'a', encoding='utf-8') as fd:
        count = fd.write(text)
        return count
