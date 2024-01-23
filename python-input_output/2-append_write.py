#!/usr/bin/python3
# 2-append_write.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Implementation of the appends function."""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
