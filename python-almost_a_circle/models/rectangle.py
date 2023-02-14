#!/usr/bin/python3
# rectangle.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a class Rectangle that inherit a class Base."""
from models.base import Base


class Rectangle(Base):
    """Create a class Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.

        Raise:
            TypeError (all args): <name attribute> must be an integer.
            ValueError (width, height): <name attribute> must be > 0.
            ValueError (x, y): <name attribute> must be >= 0
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """Set/get the width of the Rectangle."""
            return(self.__width)

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """Set/get the height of the Rectangle."""
            return(self.__height)

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if height <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """Set/get the x coordinate of the Rectangle."""
            return(self.__x)

        @x.setter
        def x(self, value):
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if x < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """Set/get the y coordinate of the Rectangle."""
            return(self.__y)

        @y.setter
        def y(self, value):
            if type(value) is not int:
                raise TypeError("y must be an integer")
            if y < 0:
                raise ValueError("y must be >= 0")
            self.__y = value