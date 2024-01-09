#!/usr/bin/python3
# Executing modules as script
if __name__ == "__main__":

    # importing functions
    from calculator_1 import add, sub, mul, div

    # defining variables
    a = 10
    b = 5
    # calling function
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
