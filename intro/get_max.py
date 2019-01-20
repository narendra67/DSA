"""Return max element in a list."""


def get_max(arr):
    """Return the max elememt among a list.

    Parameters
    ----------
    arr : [list]
        an array of integers.

    Returns
    -------
    integer
        largest element.

    """
    max_element = 0
    for i in arr:
        if i > max_element:
            max_element = i
    return max_element
