#!/usr/bin/python3
# Executing modules as script
if __name__ == "__main__":

    # importing module
    import sys

    # total arguments
    n = len(sys.argv) - 1

    # passed arguments
    if n == 0:
        print("{} arguments.".format(n))

    elif n == 1:
        print("{} argument:".format(n))

    else:
        print("{} arguments:".format(n))

    for i in range(n):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
