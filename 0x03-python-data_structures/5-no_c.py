#!/usr/bin/python3
def no_c(my_string):
    '''
        description: replaces every occurrence of c & C in
        a string
    '''
    new_str = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_str = new_str + i
    else:
        return new_str
