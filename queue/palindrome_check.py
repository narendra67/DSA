from deque import Deque


def palindrome_checker(str):
    """Check for palindrome or not."""
    dq = Deque()

    for i in range(len(str)):
        dq.addFront(str[i])

    while dq.size() > 1:
        if dq.removeFront() != dq.removeRear():
            return "Not a palindrome."

    return "It is a palindrome"
