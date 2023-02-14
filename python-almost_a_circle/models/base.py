#!/usr/bin/python3
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a class Base."""


class Base:
    """Create a class Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
