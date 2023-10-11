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
        sort_list = sorted(self)
        print(sort_list)
        return sort_list

        def __str__(self):
            '''
            prints string rep
            '''
            new_l = sorted(self)
            return super(Mylist, new_l).__str__()
