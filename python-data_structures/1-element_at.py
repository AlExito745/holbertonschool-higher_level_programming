#!/usr/bin/python3
# retrive an element from a list
def element_at(my_list, idx):

    for idx in range(0, (len(my_list) - 1)):
        if idx < 0:
            return(None)
        elif idx > (len(my_list) - 1):
            return(None)
    return(my_list[idx])
