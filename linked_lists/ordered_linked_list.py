"""An ordered liked list."""
from node import Node


class OrderedList():
    def __init__(self):
        self.head = None

    def add_old(self, item):
        temp_node = Node(item)
        previous = None
        current = self.head

        if self.head is None:
            temp_node.set_next(self.head)
            self.head = temp_node
            return str(self.head.get_data()) + " is added."
        else:
            while current is not None and item >= current.get_data():
                previous = current
                current = current.get_next()
            temp_node.set_next(current)
            if previous is None:
                self.head = temp_node
                return str(self.head.get_data()) + " is added."
            else:
                previous.set_next(temp_node)
                return str(previous.get_next().get_data()) + " is added."

    def add(self, item):
        temp_node = Node(item)
        previous = None
        current = self.head
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            temp_node.set_next(self.head)
            self.head = temp_node
        else:
            temp_node.set_next(current)
            previous.set_next(temp_node)

    def remove(self, item):
        previous = None
        current = self.head
        found = False

        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.get_data() is item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return "Item is present" if found else "Item is not present."

    def index(self, item):
        current = self.head
        found = False
        current_index = 0

        while current is not None and not found:
            if current.get_data() is item:
                found = True
            else:
                current_index += 1
                current = current.get_next()

        if found:
            return current_index
        else:
            return "Item not found in the list."

    def size(self):
        current = self.head
        size = 0
        while current is not None:
            size += 1
            current = current.get_next()

        return size

    def pop(self, position=None):
        previous = None
        current = self.head
        current_position = 0
        if position is None or position == self.size():
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
            previous.set_next(current.get_next())
            return str(current.get_data()) + " is poped."
        elif position == 0:
            self.head = current.get_next()
            return str(current.get_data()) + " is poped."
        elif position > self.size() or position < 0:
            return "Out of bound."
        else:
            while current_position is not position:
                current_position += 1
                previous = current
                current = current.get_next()
            previous.set_next(current.get_next())
            return str(current.get_data()) + " is poped."
