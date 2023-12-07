#!/usr/bin/python3
def best_score(_dictionary):
    if _dictionary is not None:
        students_number = len(_dictionary.values())
        if students_number > 0:
            score = max(_dictionary.values())
            for key in _dictionary.keys():
                if _dictionary[key] == score:
                    return key
    return None
