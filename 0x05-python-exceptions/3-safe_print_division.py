#!/usr/bin/python3
def safe_print_division(a, b):
    '''
        description: divides 2 integer and prints the result
    '''
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
        return res
    finally:
        print("Inside result: {}".format(res))
        return res
