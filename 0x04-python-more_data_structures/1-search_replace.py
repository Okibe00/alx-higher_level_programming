#!/usr/bin/python3
def check(elem, search, replace):
    '''
        description: compares search value to element
        and returns replacement if true
    '''
    if elem == search:
        return replace
    else:
        return elem


def search_replace(my_list, search, replace):
    '''
        description: replaces the occurrence of one
        element by another in a new list
    '''
    return [check(elem, search, replace) for elem in my_list]
