#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    prev = 0
    i = 0
    d = {'I': 1, 'V': 5, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'X': 10}

    if (type(roman_string) != str):
        return 0
    while(i < len(roman_string)):
        curr = d.get(roman_string[i], 0)
        if curr != 0:
            if curr > prev:
                sum += curr - prev - prev
                prev = curr
                i += 1
            else:
                sum += curr
                prev = curr
                i += 1
        else:
            return 0
    return sum
