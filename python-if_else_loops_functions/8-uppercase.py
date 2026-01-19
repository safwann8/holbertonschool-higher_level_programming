#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char = ord(c)
        if char >= ord('a') and char <= ord('z'):
            upper_c = chr(char - 32)
            print("{}".format(upper_c), end="")
        else:
            upper_c = c
            print("{}".format(upper_c), end="")
    print()
