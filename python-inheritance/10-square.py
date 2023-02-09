#!/usr/bin/python3
# 10-square.py
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
