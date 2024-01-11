#!/usr/bin/python3
# 1-my_list.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a function that checks if an object is an instance of a class."""


def is_same_class(obj, a_class):
    """ Return True or False if an instance belongs to a class."""
    if type(obj) == a_class:
        return(True)
    else:
        return(False)
