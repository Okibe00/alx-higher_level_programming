#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    '''
        description: prints an integer
    '''
    try:
        print("{:d}".format(value))
        return True
    except Exception as ec:
        print("Exception: ", ec, file=sys.stderr)
        return False
