#!/usr/bin/python3
# rectangle.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a class Rectangle that inherit a class Base."""
from models.base import Base


class Rectangle(Base):
    """Create a new instances class of Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize each new instances class of Rectangle.

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

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
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
        if value <= 0:
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
        if value < 0:
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
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of a new instances of class Rectangle."""
        return(self.height * self.width)

    def display(self):
        """Prints in stdout the new instance Rectangle with the character #."""
        if self.height == 0 and self.width == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Return the string representation of a new instance
        of the class Rectangle."""
        str = "[Rectangle] ({})".format(self.id)
        str += " {}/{} - {}/{}".format(self.x, self.y, self.width, self.height)
        return(str)

    def update(self, *args):
        """Assigns an argument to each attribute of class Rectangle."""
        if args and len(args) != 0:
            argun = 0
            for arg in args:
                if argun == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif argun == 1:
                    self.width = arg
                elif argun == 2:
                    self.height = arg
                elif argun == 3:
                    self.x = arg
                elif argun == 4:
                    self.y = arg
                argun += 1
