#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) <= 122 and ord(c) >= 97:
            c = (ord(c) - 32)
        else:
            c = ord(c)
        print(f"{c:c}", end="")
    print("")
