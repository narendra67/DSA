"""Return sum of n numbers."""


def add_nums(n):
    sum = 0
    for i in range(n):
        sum += i + 1
    return sum
