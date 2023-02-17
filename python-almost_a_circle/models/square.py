#!/usr/bin/python3
# square.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a class Square that inherits from class Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Create the class Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Create a new instances of class Square."""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter/Setter the size of the Square."""
        return(self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of a Square."""
        str = "[Square]({})".format(self.id)
        str += "{}/{} - {}".format(self.x, self.y, self.width)
        return(str)
