import copy
from typing import Any

from . import CircularQueueIterator

class CircularQueue:
    def __init__(self, max_size: int):
        if max_size <= 0:
            raise ValueError
        self._data = [None] * max_size
        self._max_size: int = max_size
        self._front = 0
        self._rear = 0
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> CircularQueueIterator:
        return CircularQueueIterator(self)
    
    def is_empty(self) -> bool:
        return len(self) == 0  

    def is_full(self) -> bool:
        return len(self) == self._max_size

    def enqueue(self, value: Any) -> None:
        if self.is_full():
            raise ValueError
        self._data[self._rear] = value
        self._rear = (self._rear + 1) % self._max_size
        self._size += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise ValueError
        value = self._data[self._front]
        self._front = (self._front + 1) % self._max_size
        self._size -= 1
        return value

    def peek(self) -> Any:
        if self.is_empty():
            raise ValueError
        return copy.deepcopy(self._data[self._front])