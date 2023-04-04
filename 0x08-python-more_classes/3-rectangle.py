#!/usr/bin/python3
"""Module for rectangle"""


class Rectangle:
    """Class Rectangle"""
    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """str"""
        if self.width == 0 or self.height == 0:
            return ""
        r = ""
        for h in range(self.height):
            for w in range(self.width):
                r = r + "#"
            r = r + "\n"
        return r

    def __init__(self, width=0, height=0):
        """construtor"""
        self.width = width
        self.height = height
