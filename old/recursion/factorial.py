def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * (i)
    return result


def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n - 1)

