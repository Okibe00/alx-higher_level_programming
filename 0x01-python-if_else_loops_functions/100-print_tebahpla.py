#!/usr/bin/python3
for i in range(122, 96, -1):
    if i == 122:
        flag = 'l'
    switch = 0
    if flag == 'l':
        flag = 'u'
    else:
        switch = -32
        flag = 'l'
    print("{}".format(chr(i + switch)), end="")
