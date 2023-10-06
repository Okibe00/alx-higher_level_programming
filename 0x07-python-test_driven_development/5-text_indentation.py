#!/usr/bin/python3
'''
prints a text with 2 new lines after\
each of these characters: ., ? and :
'''


def text_indentation(text):
    '''
    prints text
    Args:
        text: text to print
    Return:
        None
    '''
    flag = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    str_cpy = text.strip()
    txt_l = len(str_cpy)
    for i in range(txt_l):
        if str_cpy[i] in ".?:":
            print(str_cpy[i])
            print()
            flag = 1
        else:
            if flag == 1 and str_cpy[i] == " ":
                continue
            print(str_cpy[i], end="")
            flag = 0
