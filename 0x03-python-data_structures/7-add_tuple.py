#!/usr/bin/python3
def add_tuple(tupl_a=(), tupl_b=()):
    new_tupl = ()
    tupl_1 = tupl_a + (0, 0)
    tupl_2 = tupl_b + (0, 0)
    new_tuple = tupl_1[0] + tupl_2[0], tupl_1[1] + tupl_2[1]
    return new_tupl
