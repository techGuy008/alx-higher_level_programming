#!/usr/bin/python3
def print_sorted_dictionary(_dictionary):
    for key in sorted(_dictionary):
        value = _dictionary.get(key)
        print('{}: {}'.format(key, value))
