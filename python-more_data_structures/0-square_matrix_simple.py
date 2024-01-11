#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # computes the square value of all integers of a matrix
    result_list = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
    return result_list
