#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = 0
rand_num = number
if rand_num < 0:
    rand_num = rand_num * -1
    ld = -(rand_num % 10)
else:
    ld = rand_num % 10

if ld > 5:
    print(f"Last digit of {number} is {ld} and is greater than 5")
elif ld == 0 or ld == -0:
    print(f"Last digit of {number} is {ld} and is 0")
elif ld < 6 and ld != 0:
    if ld < 0:
        print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
