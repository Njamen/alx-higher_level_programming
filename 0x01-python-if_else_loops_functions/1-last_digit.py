#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
print(f"Last digit of {number} is {last}", end=" ")
if last > 0:
    print(f"and is greater than 0")
elif last == 0:
    print(f"and is 0")
else:
    print(f"and is less than 0")
