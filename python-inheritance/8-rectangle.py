#!/usr/bin/python3
# 8-rectangle.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry classparent."""

    def __init__(self, width, height):
        """Initialitation of a new rectangle."""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
