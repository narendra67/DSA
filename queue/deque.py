class Deque():
    """Deque implementation using list."""

    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.append(item)

    def addRear(self, item):
        self.deque.insert(0, item)

    def removeRear(self):
        return self.deque.pop(0)

    def removeFront(self):
        return self.deque.pop()

    def size(self):
        return len(self.deque)

    def isEmpty(self):
        return len(self.deque) == 0
