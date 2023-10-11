#!/usr/bin/python3
'''
module to write to a file
'''


def write_file(filename="", text=""):
    '''
    writes to a file
    '''
    with open(filename, 'w', encoding='utf-8') as fd:
        count = fd.write(text)
        return count
