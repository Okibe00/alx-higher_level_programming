#!/usr/bin/python3
def uppercase(str):
    switch = 0
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            switch = -32
        else:
            pass
        print("{}".format(chr(ord(i) + switch)), end="")
        switch = 0
    print()
