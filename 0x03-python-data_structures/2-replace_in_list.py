#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''
    descripton: replaces an element in a list
    '''
    list_len = len(my_list)
    if list_len == 0:
        return my_list
    if idx < 0 or idx > list_len - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
