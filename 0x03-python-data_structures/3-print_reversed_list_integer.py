#!/usr/bin/python3
def print_reversed_list_integer(list=[]):
    if list:
        list.reverse()
        for i in range(len(list)):
            print("{:d}".format(list[i]))
