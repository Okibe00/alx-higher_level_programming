#!/usr/bin/python3
'''
module creates a class that inherites from list
'''


class MyList(list):
    '''
        list class
        Attr:
            list: list object
    '''

    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        '''
            prints list
        '''
        sort_list = self
        print(sorted(sort_list))
