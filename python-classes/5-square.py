#!/usr/bin/python3
# 5-square.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a class Square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initialize a Square.

        Args:
                size(int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return(self.__size)

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(value, (int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate the area."""
        return(self.__size * self.__size)

    def my_print(self):
        """Printing a square."""

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")

        if self.size == 0:
            print("")
