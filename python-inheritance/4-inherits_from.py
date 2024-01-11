#!/usr/bin/python3
# 4-inherits_from.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a function that checks if an object is an instance that inherited
    from the specified class.
"""


def inherits_from(obj, a_class):
    """Return True or False if an instance belongs to
        a class that inherited from the specified class.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return(True)
    else:
        return(False)
