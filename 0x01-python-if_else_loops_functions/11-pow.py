#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    r = 1
    if b < 0:
        for i in range(0, -b):
            r = r / a
    else:
        for i in range(0, b):
            r = r * a;
    return r
