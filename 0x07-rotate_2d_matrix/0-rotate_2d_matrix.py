#!/usr/bin/python3
"""0. Rotate 2D Matrix"""

def rotate_2d_matrix(matrix):

    """Given an n x n 2D matrix, rotate
    it 90 degrees clockwise.
    """
    transposed_matrix = [list(row) for row in zip(*matrix)]
    
    # Reverse the order of the rows
    rotated_matrix = [list(reversed(row)) for row in transposed_matrix]
    
    return rotated_matrix
