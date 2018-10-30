def power(x, n):
    if n == 0:
        return 1
    return x*power(x, n-1)


def pow(x, n):
    """
        1. Check if n equals to 0 and return 1 if true
        2. if n is odd, return x * fun(x, n)
        3. if n is even, return y * y where y = fun(x, n/2)
        4. if n is neg, return 1/fun(x, n)  
    """

    if n == 0:
        return 1
    if n < 0:
        return 1/pow(x, -n)
    if n % 2 == 1:
        return x * pow(x, n-1)
    if n % 2 == 0:
        y = pow(x, n-1)
        return y*y
