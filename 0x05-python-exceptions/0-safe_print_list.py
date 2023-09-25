#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''
        description: prints x number of elements from list
    '''
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count = count + 1
        else:
            print()
    except IndexError:
        print()
    return count
