def base_k_strings(n, k):
    """Generate all strings with base k.

    Parameters
    ----------
    n : int
        Length of strings to be generated.
    k : int
        base of the Strings to be generated.

    """
    if n == 0:
        return []
    if n == 1:
        return [str(i) for i in list(range(k))]
    return [digit+kstring for digit in base_k_strings(1, k)
            for kstring in base_k_strings(n-1, k)]
