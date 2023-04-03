#!/usr/bin/python3
"""Class module square"""


class Square:
    """Class documentation"""
    def __init__(self, size=0):
        """init constructor
        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
