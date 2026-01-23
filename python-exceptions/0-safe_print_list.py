#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed += 1
        print()
    except IndexError:
        print()
    return print
