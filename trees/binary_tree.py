"""Binary Tree class and its methods."""


class BinaryTreeNode:
    """Node of a binary Tree.

    Node of binary holds three values:
    data - data of the node
    left - a pointer to left subtree
    right - a pointer to right subtree

    """

    def __init__(self, data):
        """Set data of the node on creation."""
        self.data = data  # root node
        self.left = None  # left child
        self.right = None  # right chile

    def set_data(self, data):
        """Set the data of the node."""
        self.data = data

    def get_data(self):
        """Get the node's data."""
        return self.data

    def get_left(self):
        """Get the left child of the node."""
        return self.left

    def get_right(self):
        """Get the right child of the node."""
        return self.right
