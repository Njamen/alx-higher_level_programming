#!/usr/bin/python3
""" class Square module"""


class Square:
    def __init__(self, size=0):
        """init square
        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
