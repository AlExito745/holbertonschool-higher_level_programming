#!/usr/bin/python3
def safe_print_integer(value):
    # function that print an integer using string format
    try:
        print("{:d}".format(value))
        return(True)
    except(TypeError, ValueError):
        return(False)
