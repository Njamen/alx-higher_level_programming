#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary)
    for x in a:
        print("{a1}: {a2}".format(a1=x, a2=a_dictionary.get(x)))
