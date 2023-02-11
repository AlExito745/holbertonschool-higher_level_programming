#!/usr/bin/python3
# 1-write_file.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a function that writes a string within to a text file."""


def write_file(filename="", text=""):
    """Implementation of the write function."""
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(text))
