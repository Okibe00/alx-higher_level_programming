#!/usr/bin/python3
'''
prints my name is <first name> <last name>
'''


def say_my_name(first_name, last_name=""):
    '''
        prints <first name> <last name>
        Args:
            first_name: ........
            last_name:.........
        Return:
            None
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if len(last_name) == 0:
        print(f"My name is {first_name} ")
    else:
        print(f"My name is {first_name} {last_name}")
