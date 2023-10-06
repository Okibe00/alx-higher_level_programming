#!/usr/bin/python3
'''
    prints a square
'''


def print_square(size):
    '''
        prints a square

        Args:
            size: size of square
        Return:
            None
    '''
    symbol = "#"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print(symbol * size)
