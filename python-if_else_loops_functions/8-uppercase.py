#!/usr/bin/python3
def islower(c):
    c = ord(c)
    if c >= ord('A') and c <= ord('Z'):
        return True
    else:
        return False
