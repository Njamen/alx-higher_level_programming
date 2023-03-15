#!/usr/bin/python
def number_keys(a_dictionary):
    if not a_dictionary:
        return 0
    i = 0
    for x in a_dictionary:
        i = i + 1
    return i
