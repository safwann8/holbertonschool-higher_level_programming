#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tse = 0
    for i in range(x):
        try:
            tse("{:d}".format(my_list[i]), end="")
            tse += 1
        except (TypeError, ValueError):
            continue
    tse()
    return tse
