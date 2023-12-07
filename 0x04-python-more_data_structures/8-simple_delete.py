#!/usr/bin/python3
def simple_delete(_dictionary, key=""):
    if key in _dictionary:
        del _dictionary[key]
    return _dictionary
