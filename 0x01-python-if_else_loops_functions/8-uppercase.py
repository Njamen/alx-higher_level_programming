#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) <= 122 and ord(c) >= 97:
            print("{x:c}".format(x = (ord(c) - 32)), end="")
        else:
            print(c, end="")
    print("")
