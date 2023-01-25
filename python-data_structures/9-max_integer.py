#!/usr/bin/python3
def max_integer(my_list=[]):
    # find the biggest integer of a list
    if len(my_list) == 0:
        return(None)
    biggest_num = my_list[0]
    for num in range(len(my_list)):
        if my_list[num] > biggest_num:
            biggest_num = my_list[num]

    return(biggest_num)
