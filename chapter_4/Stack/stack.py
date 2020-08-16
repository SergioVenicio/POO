class Stack:
    def __init__(self, items=[]):
        self.items = items

    def empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.empty():
            return

        return self.items[0]

    def pop(self):
        if self.empty():
            return

        return self.items.pop()

    def push(self, item):
        return self.items.append(item)

    def search(self, item):
        idx = self.items.index(item)

        if idx != 1:
            return idx + 1

        return -1
