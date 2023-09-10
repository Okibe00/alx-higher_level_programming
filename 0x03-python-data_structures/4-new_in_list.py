#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''
    description: replace element at an index
    without modifying original list
    '''
    list_len = len(my_list)
    if list_len == 0:
        return my_list
    if idx < 0 or idx > list_len - 1:
        return my_list
    else:
        list_cpy = my_list[:]
        list_cpy[idx] = element
        return list_cpy
