#!/usr/bin/python3
def multiple_returns(sentence):
    _tupl = ()
    if len(sentence) == 0:
        _tupl = 0, "None"
    else:
        _tupl = len(sentence), sentence[0]
    return _tupl
