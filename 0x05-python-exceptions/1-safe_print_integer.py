#!/usr/bin/python3
def safe_print_integer(value):
    '''
        description: prints an integer
    '''
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
