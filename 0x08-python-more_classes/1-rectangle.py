#!/usr/bin/python3
"""Module for rectangle"""


class Rectangle:
    """Class Rectangle"""
    def width(self):
        """get width"""
        return self.__width

    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """get heigth"""
        return self.__height

    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """construtor"""
        self.width = width
        self.height = height
