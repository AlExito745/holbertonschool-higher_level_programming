#!/usr/bin/python3
# 3-is_kind_of_class.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a function that checks if an object is an instance of a class that
    inherited from."""


def is_kind_of_class(obj, a_class):
    """Return True or False if an instance belongs to
        a class or class inherited."""
    if isinstance(obj, a_class):
        return(True)
    else:
        return(False)
