#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char = ord(c)
        if ord('a') <= char <= ord('z'):
            c = chr(char - 32)
        print("{}".format(c), end="")
    print()
