#!/usr/bin/python3
# Excecuting module as script
if __name__ == "__main__":

    # importing module
    import sys

    # total arguments
    n = len(sys.argv)

    # addition of numbers
    sum = 0
    # using argparse module
    for i in range(n - 1):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
