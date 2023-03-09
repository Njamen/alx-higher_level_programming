#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    a = 1
    b = 2
    print("{x} + {y} = {z}".format(x=a, y=b, z=add(a, b)))
