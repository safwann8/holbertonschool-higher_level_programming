#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    list = []
    for i in my_list:
        if i not in list:
            res += i
            list.append(i)
    return res
