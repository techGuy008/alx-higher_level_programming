#!/usr/bin/python3
def complex_delete(_dictionary, value):
    if value is not None:
        keys = list(_dictionary.keys())
        for key in keys:
            if _dictionary[key] == value:
                del _dictionary[key]
    return _dictionary
