#!/usr/bin/python3
'''
module to write to a file
'''
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    '''
    all arguments to a Python list, and then save them to a file
    '''
    item_list = list()
    num_arg = len(sys.argv)
    for i in range(1, num_arg):
        item_list.append(sys.argv[i])
    else:
        save_to_json_file(item_list, "add_item.json")
        return load_from_json_file("add_item.json")


if __name__ == "__main__":
    add_items()
