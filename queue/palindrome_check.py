from deque import Deque


def palindrome_checker(a_string):
    """Check for palindrome or not using deque."""
    _dq = Deque()

    for i, str_val in enumerate(a_string):
        _dq.addFront(str_val)

    while _dq.size() > 1:
        if _dq.removeFront() != _dq.removeRear():
            return "Not a palindrome."

    return "It is a palindrome"


# implementation from interactive python
def palindrome_checker_ip(a_string):
    """FROM: Interactive Python - Check for palindrome or not using deque."""
    chardeque = Deque()

    for index, value in enumerate(a_string):
        chardeque.addFront(value)

    still_equal = True

    while chardeque.size() > 1 and still_equal:
        first = chardeque.removeFront()
        last = chardeque.removeRear()

        if first != last:
            still_equal = False

    return still_equal
