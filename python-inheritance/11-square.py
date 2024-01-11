#!/usr/bin/python3
# 11-square.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square using a class base Rectangle."""

    def __init__(self, size):
        """Initialitation of a new square."""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        string = "[" + str(self.__class__.__name__) + "]"
        string += " " + str(self.__size) + "/" + str(self.__size)
        return string
