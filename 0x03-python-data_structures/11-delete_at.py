#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    '''
        description: deletes element at idx
    '''
    list_len = len(my_list)
    if list_len == 0:
        return my_list

    if idx < 0 or idx > list_len - 1:
        return my_list
    else:
        del my_list[idx]
        return my_list
