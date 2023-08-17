#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        alt_matrix = []
        for column in row:
            alt_matrix.append(column ** 2)
        new_matrix.append(alt_matrix)

    return (new_matrix)
