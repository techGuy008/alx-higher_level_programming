#!/usr/bin/python3
def max_integer(_list=[]):
    if len(_list) == 0:
        return "None"
    else:
        max = _list[0]
        for i in range(len(_list)):
            if _list[i] > max:
                max = _list[i]
        return max
