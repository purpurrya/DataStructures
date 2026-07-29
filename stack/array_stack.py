import copy
from typing import Any

from array.dynamic_array import DynamicArray

class ArrayStack:
    def __init__(self):
        self._data = DynamicArray()

    def is_empty(self) -> bool:
        return self._data.is_empty()

    def push(self, value: Any) -> None:
        self._data.insert(value)

    def pop(self) -> Any:
        if self.is_empty():
            raise ValueError
        return self._data.delete(len(self._data) - 1)

    def peek(self) -> Any:
        if self.is_empty():
            raise ValueError
        return self.get(len(self._data) - 1)

    def get(self, index: int) -> Any:
        if index < 0 or index >= len(self._data):
            raise IndexError
        return copy.deepcopy(self._data.get(index))
