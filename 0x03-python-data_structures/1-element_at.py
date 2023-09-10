#!/usr/bin/python3
def element_at(my_list, idx):
    '''
    prints the element at index idx
    '''
    list_len = len(my_list)
    if list_len == 0:
        return None
    if idx < 0 or idx > list_len - 1:
        return None
    else:
        return my_list[idx]
