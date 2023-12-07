#!/usr/bin/python3
def roman_intVal(r):
    dict = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    return dict[r] if r in dict else 0 

def roman_to_decimal(str):
    res = 0
    i = 0
    while i < len(str):
        str1 = roman_intVal(str[i])
        if i + 1 < len(str):
            str2 = roman_intVal(str[i + 1])
            if str1 >= str2:
                res += str1
            else:
                res += str2 - str1
                i += 1
        else:
            res += str1
        i += 1
    return res
