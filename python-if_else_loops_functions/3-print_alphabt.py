#!/usr/bin/python3
for lwcas in range(97, 123):
    lwcas = chr(lwcas)
    if lwcas not in "qe":
        print("{}".format(lwcas), end="")
