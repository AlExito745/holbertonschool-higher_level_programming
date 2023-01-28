#!/usr/bin/python3
def safe_print_integer(value):
    # function that print an integer using string format
    if isinstance(value, (int, float, str, list, tuple, dict, set, None)):
        try:
            print("{:d}".format(value))
            return(True)
        except(TypeError, ValueError):
            return(False)
