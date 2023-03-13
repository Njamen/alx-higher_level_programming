#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for x in range(len(my_list)):
        print("{n:d}".format(n=my_list[x]))
