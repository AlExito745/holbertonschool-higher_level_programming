#!/usr/bin/python3
# 5-save_to_json_file.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a function that writes an object to a tex file
    using a JSON representation."""


def save_to_json_file(my_obj, filename):
    """Implementation of the JSON representation."""
    import json
    with open(filename, "w") as f:
        json.dump(my_obj, f)
