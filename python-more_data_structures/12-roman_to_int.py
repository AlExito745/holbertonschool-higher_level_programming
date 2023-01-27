#!/usr/bin/python3
def roman_to_int(roman_string):
    # function that convert roman numeral to an integer
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not roman_string or None:
        return(0)

    total = 0
    i = 0

    while(i < len(roman_string)):
        s1 = values[roman_string[i]]
        if (i + 1 < len(roman_string)):
            s2 = values[roman_string[i+1]]
            if (s1 >= s2):
                total = total + s1
                i = i + 1
            else:
                total = total - s1
                i = i + 1
        else:
            total = total + s1
            i = i + 1
    return(total)
