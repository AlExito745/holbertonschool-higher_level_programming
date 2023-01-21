#!/usr/bin/python3
# Executing modules as script
if __name__ == "__main__":

    # importing add 
    from add_0 import add

    # defining variables
    a = 1
    b = 2

    # calling function
    add(a, b)
    print("{} + {} = {}".format(a, b, add(a, b)), end="\n")
