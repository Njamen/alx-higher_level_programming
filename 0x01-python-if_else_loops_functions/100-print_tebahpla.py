#!/usr/bin/python3
upper = 0
for i in range(122, 96, -1):
    if upper == 1:
        i = i - 32
    print(f"{i:c}", end="")
    upper = (upper + 1) % 2
