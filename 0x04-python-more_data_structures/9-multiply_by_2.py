#!/usr/bin/python3
def multiply_by_2(_dictionary):
    new_dict = _dictionary.copy()
    for key in new_dict.keys():
        new_dict[key] *= 2
    return new_dict
