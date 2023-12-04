#!/usr/bin/python3
def no_c(str):
    str2 = str.translate({ord(i): None for i in 'cC'})
    return str2
