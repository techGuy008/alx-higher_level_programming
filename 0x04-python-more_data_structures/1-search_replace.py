#!/usr/bin/python3
def search_replace(_list, search, replace):
    result = [num if num != search else replace for num in _list]
    return result
