#!/usr/bin/python3
# 8-class_to_json.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a function that returns the dictionary
    for JSON serializato of an object."""


def class_to_json(obj):
    """Return the dictionary of a simple data structure."""
    return(obj.__dict__)
