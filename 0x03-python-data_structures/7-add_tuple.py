#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''
        description: adds two tuples
    '''
    len_tup_a = len(tuple_a)
    len_tup_b = len(tuple_b)

    tup_a_f = 0
    tup_a_s = 0
    tup_b_f = 0
    tup_b_s = 0

    if len_tup_a == 1:
        tup_a_f = tuple_a[0]

    if len_tup_b == 1:
        tup_b_f = tuple_b[0]

    if len_tup_a >= 2:
        tup_a_f = tuple_a[0]
        tup_a_s = tuple_a[1]

    if len_tup_b >= 2:
        tup_b_f = tuple_b[0]
        tup_b_s = tuple_b[1]

    new_tuple = (tup_a_f + tup_b_f), (tup_a_s + tup_b_s)
    return new_tuple
