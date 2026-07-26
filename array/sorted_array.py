from collections.abc import Callable
from typing import Any
from array import array


class SortedArray:
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

    def linear_search(self, target: Any) -> int | None:
        for index in range(self._size):
            if self._array[index] == target:
                return index
        return None
    
    def binary_search(self, target: Any) -> int | None:
        left = 0
        right = self._size - 1
        while left <= right:
            mid_index = (left + right) // 2
            mid_val = self._array[mid_index]
            if mid_val == target:
                return mid_index
            elif mid_val > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return None 
    
    def binary_search_first_target(self, target: Any) -> int | None:
        result = None
        left = 0
        right = self._size - 1
        while left <= right:
            mid_index = (left + right) // 2
            mid_val = self._array[mid_index]
            if mid_val == target:
                result = mid_index
                right = mid_index - 1
            elif mid_val > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return result
    
    def traverse(self, callback: Callable) -> None:
        for index in range(self._size):
            callback(self._array[index])

    def insert(self, value: Any) -> None: 
        if self._size >= self._max_size:
            raise ValueError
        for index in range(self._size, 0, -1):
            if self._array[index - 1] <= value:
                self._array[index] = value
                self._size += 1
                return
            else:
                self._array[index] = self._array[index - 1]
        self._array[0] = value
        self._size += 1

    def delete(self, target: Any) -> None:
        index = self.linear_search(target)
        if index is None:
            raise ValueError
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1
    
    def delete_by_index(self, index: int) -> None:
        if index < 0 or index > self._size:
            raise IndexError
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1