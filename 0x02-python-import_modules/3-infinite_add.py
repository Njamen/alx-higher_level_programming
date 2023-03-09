#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    ll = len(argv) - 1
    if ll == 0:
        print("0")
    else:
        s = 0
        for x in argv[1:]:
            s = s + int(x)
        print(s)
