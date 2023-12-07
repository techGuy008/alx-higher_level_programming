#!/usr/bin/python3
def get_ponderated_promedium(scores):
    list_promediums = list(map(lambda a: a[0] * a[1], scores))
    return sum(list_promediums)


def get_sum_weight(scores):
    list_weights = list(map(lambda a: a[1], scores))
    return sum(list_weights)


def weight_average(_list=[]):
    if len(_list) == 0:
        return 0
    else:
        average = get_ponderated_promedium(_list) / get_sum_weight(_list)
        return average
