def gen_binary_strings(n):
    """Generate all binary strings with n bits."""
    if n == 0:
        return []
    if n == 1:
        return ['0', '1']
    return [digit+bitstring for digit in gen_binary_strings(1)
            for bitstring in gen_binary_strings(n-1)]