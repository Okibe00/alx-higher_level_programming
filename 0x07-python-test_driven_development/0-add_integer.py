#!/usr/bin/python3
'''
    Module creates a contains a funtion that adds two number
'''


def add_integer(a, b=98):
    '''
        adds two numbers
        Args:
            a: number
            b: number
        Return:
            integer
    '''
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")

    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")

    num1 = int(a)
    num2 = int(b)
    return num1 + num2
