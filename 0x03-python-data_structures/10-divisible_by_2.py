#!/usr/bin/python3
def divisible_by_2(_list=[]):
    _list2 = []
    for i in range(len(_list)):
        if _list[i] % 2 == 0:
            _list2.append(True)
        else:
            _list2.append(False)
    return _list2
