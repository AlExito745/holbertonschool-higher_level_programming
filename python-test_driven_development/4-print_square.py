#!/usr/bin/python3
def print_square(size):
    """Prints a square with the character #.

    Args:
        Size: Is the length of the square.
    Raises:
        TypeError: If value of size is not a integer.
        ValueError:  If value of size is less than 0.
        TypeError: If value of size is a float and less than 0.
    """

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    for i in range(0, size):
        [print("#", end="") for j in range(size)]
        print("")
