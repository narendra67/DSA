"""Stack datastructure in python."""


class Stack():
    """Stack implementation using python list."""

    def __init__(self):
        self.stack = []

    def is_empty(self):
        """Check whether the stack is empty or not."""
        return self.stack == []

    def push(self, ele):
        """Push an element into stack."""
        self.stack.append(ele)

    def pop(self):
        """Remove/Pop top element of the stack."""
        stack_length = len(self.stack)
        if (stack_length) == 0:
            return "Stack is empty, cannot perform a pop operation."

        return self.stack.pop()

    def size(self):
        """Size of the stack."""
        return len(self.stack)

    def peek(self):
        """Return top most element on the stack."""
        stack_length = len(self.stack)
        if stack_length == 0:
            return "Stack is empty."

        return self.stack[len(self.stack)-1]
