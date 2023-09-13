#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
        description: adds uniwue elements in a list
    '''
    sum = 0
    for i in set(my_list):
        sum = sum + i
    return (sum)
