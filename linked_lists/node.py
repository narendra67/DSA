"""A node object for linked list."""


class Node():
    """A node with a data field to hold the value and a next field to hold the
        reference to next node.
    """
    def __init__(self, value):
        self.data = value
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, value):
        self.data = value

    def set_next(self, node):
        self.next = node
