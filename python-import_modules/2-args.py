#!/usr/bin/python3
# Executing modules as script
if __name__ == "__main__":

    # importing module
    import sys

    # total arguments
    n = len(sys.argv) - 1
    print("{} argument:".format(n))

    # arguments passed
    for i in range(1, n):
        print("{}: {}".format(n + 1, sys.argv[i + 1]))
