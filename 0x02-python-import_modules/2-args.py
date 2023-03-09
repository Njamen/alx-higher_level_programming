#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    ll = len(argv) - 1
    if ll == 1:
        print("1 argument:")
    elif ll == 0:
        print("0 arguments.")
    else:
        print(f"{ll} arguments:")
    i = 1
    for x in argv[1:]:
        print(f"{i}: {x}")
        i = i + 1
