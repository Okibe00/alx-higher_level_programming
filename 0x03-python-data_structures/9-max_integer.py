#!/usr/bin/python3
def max_integer(my_list=[]):
    '''
        description: find max element in a list
    '''
    list_len = len(my_list)
    if list_len == 0:
        return None
    else:
        my_list.sort()
        return my_list[-1]
