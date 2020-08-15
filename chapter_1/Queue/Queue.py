from abc import ABCMeta, abstractmethod


class QueueInterface(metaclass=ABCMeta):
    @abstractmethod
    def enqueue(self, obj: object):
        raise NotImplementedError

    @abstractmethod
    def dequeue(self) -> object:
        raise NotImplementedError

    @abstractmethod
    def is_empty(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def peek(self) -> object:
        raise NotImplementedError


class BankQueue(QueueInterface):
    def __new__(cls, items=[]):
        instance = super(BankQueue, cls).__new__(cls)

        if not isinstance(items, list):
            raise AttributeError('Invalid items!')

        return instance

    def __init__(self, items=[]):
        self.items = items

    def enqueue(self, item):
        self.items = self.items + [item]

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0
