"""Algo to check sorted order of an array."""


def check_sorted_order(array):
    """Check if the array is in a sorted order using recursion."""
    # Base case
    if len(array) is 0:
        return 'Empty list'
    if len(array) is 1:
        return True

    # Recursive case
    return array[0] <= array[1] and check_sorted_order(array[1:])
