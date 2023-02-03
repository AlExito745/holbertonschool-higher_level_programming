#!/usr/bin/python3
# 1-rectangle.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the class rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the current widht of the rectangle."""
        return(self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Get/set the current height of the rectangle."""
        return(self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")
