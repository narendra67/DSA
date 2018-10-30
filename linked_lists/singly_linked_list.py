"""Node of a singly linked list."""


class Node:
    """a node for a singly linked list."""

    # constructor
    def __init__(self):
        """Declare a constructor function."""
        self.data = None
        self.next = None

    def set_data(self, data):
        """Set data field of the node."""
        self.data = data

    def get_data(self):
        """Get data from the node."""
        return self.data

    def set_next(self, next):
        """Set next field of the node."""
        self.next = next

    def get_next(self):
        """Get next field of the node."""
        return self.next

    def has_next(self):
        """Return true if next field is not NULL."""
        return self.next is not None
