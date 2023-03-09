#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    print("{x} + {y} = {z}".format(x=a, y=b, z=add(a, b)))
    print("{x} - {y} = {z}".format(x=a, y=b, z=sub(a, b)))
    print("{x} + {y} = {z}".format(x=a, y=b, z=mul(a, b)))
    print("{x} / {y} = {z}".format(x=a, y=b, z=div(a, b)))
