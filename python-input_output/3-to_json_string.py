#!/usr/bin/python3
# 3-to_json_string.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a function that returns the
    JSON representation of an object (string)."""


def to_json_string(my_obj):
    """Implementation of the JSON representation."""
    import json
    return(json.dumps(my_obj))
