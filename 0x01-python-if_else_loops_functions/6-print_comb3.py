#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            if i == 0 and j == 1:
                print("{x:d}{y:d}".format(x=i, y=j), end="")
            else:
                print(", {x:d}{y:d}".format(x=i, y=j), end="")
print("")
