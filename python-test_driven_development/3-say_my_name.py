#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Function that print any name and last name.

    Args:
        The arguments are strings.
    Raises:
        TypeError: If arguments are not strings.
    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
