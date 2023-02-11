#!/usr/bin/python3
"""Define a function that read a text file and print it to stdout."""


def read_file(filename=""):
    """Implementation of the function."""
    with open('my_file_0.txt', encoding="utf-8") as f:
        print(f.read())
