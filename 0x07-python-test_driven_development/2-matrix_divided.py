#!/usr/bin/python3
'''
divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    '''
        divides all elements of a matrix
        Args:
            matrix: matrix
            div: divisor
        Return: matrix of quotients
    '''
    if not isinstance(matrix[0], list):
        raise TypeError
    else:
        row_s = len(matrix[0])
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    quo_l = list()
    for i in range(len(matrix)):
        if len(matrix[i]) > row_s or len(matrix[i]) < row_s:
            raise TypeError('Each row of the matrix must have the same size')
        elif type(matrix[i]) != list:
            raise TypeError()
        temp_l = list()
        for j in range(len(matrix[i])):
            val = matrix[i][j]
            if not isinstance(val, (float, int)):
                raise TypeError('matrix must be a matrix' +
                                '(array of arrays of integers/floats)')
            try:
                quotient = round(val / div, 2)
            except Exception:
                raise TypeError
            temp_l.append(quotient)
        else:
            quo_l.append(temp_l[:])
    return quo_l
