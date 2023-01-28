#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # function that print the first "x" element of a list
    counter = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter = counter + 1
        except(ValueError, TypeError):
            continue
    print("")
    return(counter)
