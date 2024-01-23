#!/usr/bin/python3
# 0-read_file.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a function that read a text file and print it to stdout."""


def read_file(filename=""):
    """Implementation of the function."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
