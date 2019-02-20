"""A unordered Linked List."""
from node import Node


class Unordered_List():

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        """Add an element to the head."""
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp
        return str(temp.get_data()) + " added to Head."

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, value):

        current = self.head
        found = False

        while current is not None and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, value):
        previous = None
        current = self.head
        removed = False

        while current is not None and not removed:
            if current.get_data() == value:
                previous.set_next(current.get_next())
                removed = True
            else:
                previous = current
                current = current.get_next()
        return removed

    def remove_new(self, value):
        previous = None
        current = self.head
        found = False

        # Finding the node to be removed
        while current is not None and not found:
            if current.get_data() == value:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return str(current.get_data()) + ' successfully removed.'

    def append(self, value):
        """Add an element to the end of the unordered list."""
        temp_node = Node(value)
        current = self.head

        while current.get_next() is not None:
            current = current.get_next()

        current.set_next(temp_node)

        return current.get_next().get_data()

    def insert(self, value, position):
        """Insert the node at given position."""
        temp_node = Node(value)
        current_position = 0
        previous = None
        current = self.head

        if position == 0:
            return self.add(value)

        if position is self.size():
            return self.append(value)

        if position >= self.size():
            return "Index out of range."

        while current_position is not position:
            previous = current
            current = current.get_next()
            current_position += 1

        temp_node.set_next(current)
        previous.set_next(temp_node)

        return previous.get_next().get_data()

    def pop(self, position=False):
        """Remove the last element or the position mentioned.

        1. Check if position is given else remove last element if present.
        2. If position is given than set previous node next pointer to current
           nodes next.
        """
        previous = None
        current = self.head
        if not position or position is self.size():
            print("in pop")
            if self.is_empty():
                return "The list is already empty."
            else:
                while current.get_next() is not None:
                    previous = current
                    current = current.get_next()

                return previous.set_next(None)

        if position == 0:
            self.head = current.get_next()
            return self.head.get_data()

        current_pos = 0

        while current_pos is not position:
            print(current_pos, position, current)
            previous = current
            current = current.get_next()
            current_pos += 1

        previous.set_next(current.get_next())

        return previous.get_data()

    def index(self, value):
        """Find index of the given value.

        1. Search for the value while tracking its current position.
        2. If the value is found return its index else return not found in
           list.
        """
        current_index = 0
        current = self.head
        found = False

        while current is not None and not found:
            if current.get_data() is value:
                found = True
            else:
                current_index += 1
                current = current.get_next()

        if found:
            return current_index
        else:
            return "Node is not found in the list."
