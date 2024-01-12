#!/usr/bin/python3
"""N queens puzzle
"""
import sys


def printSolution(board):
    """print the solution
    """
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)
