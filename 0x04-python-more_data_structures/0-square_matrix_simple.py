#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
        description: computes teh square of all integers in a 2D-array
    '''
    return [[col ** 2 for col in row] for row in matrix]
