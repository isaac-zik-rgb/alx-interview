#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    # Reverse the matrix
    reversed_matrix = matrix[::-1]

    # Get the number of columns and rows
    columns, rows = len(reversed_matrix), len(reversed_matrix[0])

    # Create a new matrix with rotated values
    rotated_matrix = [[reversed_matrix[i][j] for i in range(columns)] for j in range(rows)]

    return rotated_matrix

