#!/usr/bin/python3
"""MOdule documentation"""


def add_integer(a, b=98):
    """Function add"""
    if not isinstance(a, float):
        if not isinstance(a, int):
            raise TypeError("a must be an integer")
    else:
        a = int(a)
    if not isinstance(b, float):
        if not isinstance(b, int):
            raise TypeError("b must be an integer")
    else:
        b = int(b)
    return a + b


