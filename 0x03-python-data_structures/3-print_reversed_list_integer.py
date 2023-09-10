#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
        description: prints a list in reverse
    '''
    list_cpy = my_list[:]
    list_cpy.reverse()
    for i in range(len(list_cpy)):
        print("{:d}".format(list_cpy[i]))
