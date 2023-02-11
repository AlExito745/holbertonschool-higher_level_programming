#!/usr/bin/python3
# 6-load_from_json_file.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a function that creates an object from a "JSON file."""


def load_from_json_file(filename):
    """Implementation of the JSON representation."""
    import json
    with open(filename, encoding="utf-8") as f:
        return(json.load(f))
