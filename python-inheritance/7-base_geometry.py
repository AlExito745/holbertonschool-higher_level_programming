#!/usr/bin/python3
# 7-base_geometry.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a class."""


class BaseGeometry:
    """Implementation of the BaseGeometry class."""

    def area(self):
        """Define a area of an object."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Implementation of a validator."""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
