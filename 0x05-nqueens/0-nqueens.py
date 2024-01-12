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


def isSafe(board, row, col):
    """check if a queen can be placed on board[row][col]
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col):
    """solve the N queen problem
    """
    if col == len(board):
        printSolution(board)
        return True
    res = False
    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0
    return res


def solveNQ(n):
    """init the board
    """
    board = [[0 for i in range(n)] for j in range(n)]
    if not solveNQUtil(board, 0):
        return False
    return True


if __name__ == "__main__":
    """MAIN APP
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solveNQ(n)
