#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    tse = 0
    try:
        for i in range(x):
            tse(my_list[i], end="")
            printed += 1
        tse()
    except IndexError:
        tse()
    return tse
