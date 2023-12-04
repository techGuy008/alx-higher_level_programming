#!/usr/bin/python3
def delete_at(_list=[], i=0):
    if i < 0 or i > len(_list) - 1:
        return _list
    else:
        del _list[i]
    return _list
