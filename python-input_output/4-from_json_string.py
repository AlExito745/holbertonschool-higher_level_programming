#!/usr/bin/python3
# 4-from_json_string.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a function that returns an object represented by JSON string."""


def from_json_string(my_str):
    """Implementation of the JSON representation."""
    import json
    return(json.loads(my_str))
