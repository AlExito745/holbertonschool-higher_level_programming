#!/usr/bin/python3
# 9-student.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a class Student that define a student."""


class Student:
    """Create a class Student."""

    def __init__(self, first_name, last_name, age):
        """Initialization of the class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary of a class Student."""
        return(self.__dict__)
