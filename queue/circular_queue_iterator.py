import copy
from typing import Any

from array.static_array import StaticArray

class CircularQueueIterator:
    def __init__(self, circular_queue):
        self._circular_queue = circular_queue
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._circular_queue):
            raise StopIteration
        value = self._circular_queue._data[(self._circular_queue._front + self._index) % self._circular_queue._max_size]
        self._index += 1
        return copy.deepcopy(value)