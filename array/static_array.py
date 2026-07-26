from collections.abc import Callable
from typing import Any
from array import array


class UnsortedArray:
    def __init__(self, max_size, typecode='l'):
        self._array = array(typecode, [0]) * max_size
        self._max_size: int = max_size 
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> Any:
        if index < 0 or index >= self._size:
            raise IndexError
        return self._array[index]

    def insert(self, new_entry: Any) -> None:
        if self._size >= self._max_size:
            raise ValueError 
        else:
            self._array[self._size] = new_entry
            self._size += 1

    def delete(self, index: int) -> None:
        if self._size == 0 or index < 0 or index >= self._size:
            raise ValueError
        else:
            self._array[index] = self._array[self._size - 1]
            self._array[self._size - 1] = 0  # Для array нужно число, не None
            self._size -= 1

    def find(self, target: Any) -> int | None:
        for index in range(self._size):
            if self._array[index] == target:
                return index
        return None

    def find_all(self, target: Any) -> list[int]:
        result = []
        for index in range(self._size):
            if self._array[index] == target:
                result.append(index)
        return result
    
    def traverse(self, callback: Callable[[Any], Any]) -> None:
        for index in range(self._size):
            callback(self._array[index])

    def max_min(self) -> tuple[int, Any, int, Any]:
        if self._size == 0:
            raise ValueError
        max_index = 0
        min_index = 0
        for index in range(1, self._size):
            if self._array[index] > self._array[max_index]:
                max_index = index
            if self._array[index] < self._array[min_index]:
                min_index = index
        return max_index, self._array[max_index], min_index, self._array[min_index]