"""A Queue class."""


class Queue():
    """A Queue implementation using list."""

    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        """Size of the queue."""
        return len(self.queue)

    def is_empty(self):
        """Return if the queue is empty or not."""
        return len(self.queue) == 0
