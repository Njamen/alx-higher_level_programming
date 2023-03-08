#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{ch:d}".format(ch=i))
    elif i < 10:
        print("0{ch:d}".format(ch=i), end=", ")
    else:
        print("{ch:d}".format(ch=i), end=", ")
