#!/usr/bin/python3
def new_in_list(list, i, element):
    copy = list.copy()
    if i < 0 or i > len(list) - 1:
        return list.copy()
    else:
        copy[i] = element
        return copy
