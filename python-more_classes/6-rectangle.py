#!/usr/bin/python3
# 6-rectangle.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the class rectangle."""
        self.width = width
        self.height = height

        # When a rectangle is created, this is
        # add to the number_of_instances
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the current widht of the rectangle."""
        return(self.__width)

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the rectangle."""
        return(self.__height)

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return(self.__width * self.__height)

    def perimeter(self):
        """Return the rectangle perimeter."""
        if (self.__width == 0 or self.__height == 0):
            return(0)
        return(2 * (self.__width + self.__height))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """

        if (self.__width == 0 or self.__height == 0):
            return("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return("".join(rect))

    def __repr__(self):
        """Return the formal representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return(rect)

    def __del__(self):
        """Deleting a rectangle"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
