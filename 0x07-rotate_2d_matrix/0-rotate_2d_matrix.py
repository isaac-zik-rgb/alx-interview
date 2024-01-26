#!/usr/bin/python3
"""0. Rotate 2D Matrix"""

def rotate_2d_matrix(matrix):

    """Given an n x n 2D matrix, rotate
    it 90 degrees clockwise.
    """
    reversed_matrix = matrix[::-1]
    columns = len(reversed_matrix)
    rows = len(reversed_matrix[0])
    myArry = [[0] * columns for _ in range(rows)]
    for i in range(columns):
        for j in range(rows):
            myArry[j][i] = reversed_matrix[i][j]
    
    return myArry
