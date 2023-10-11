#!/usr/bin/python3
'''
reads a file
'''


def read_file(filename=""):
    '''
    reads a file
    '''
    with open(filename, encoding="utf-8") as fp:
        print(fp.read(), end="")
