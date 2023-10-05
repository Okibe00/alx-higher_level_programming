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

    try:
        num1 = int(a)
        num2 = int(b)
    except (ValueError, NameError, TypeError):
        raise ValueError("not a number")
    if num1 + 1 > 1e308 or num2 + 1 > 1e308:
        raise OverflowError("value too large")
    return num1 + num2
