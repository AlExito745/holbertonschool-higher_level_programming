#!/usr/bin/python3
# 1-my_list.py
# Alex Nuñez <5694@holbertonstudents.com>
"""Create a class called MyList that inherits from classbase list."""


class MyList(list):
    """Represent a derived class Mylist."""

    def print_sorted(self):
        """Function that print a list in ascending sort."""
        print(sorted(self))
