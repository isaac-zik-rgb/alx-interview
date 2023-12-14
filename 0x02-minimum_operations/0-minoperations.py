#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ Method that calculates the fewest number of operations
        needed to result in exactly n H characters in the file """

    operation = 0
    div = 2

    if n <= 1:
        return 0
    while n > 1:
        if n % div == 0:
            operation += div
            n /= div
        else:
            div += 1
    return operation
