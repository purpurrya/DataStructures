from typing import Any, Optional

class DynamicArray:
    def __init__(self, initial_capacity: int = 10):
        self._capacity = initial_capacity
        self._size = 0
        self._array = [None] * self._capacity

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> Any:
        if index < 0 or index >= self._size:
            raise IndexError
        return self._array[index]

    def __setitem__(self, index: int, value: Any) -> None:
        if index < 0 or index >= self._size:
            raise IndexError
        self._array[index] = value

    def is_empty(self) -> bool:
        return self._size == 0

    def insert(self, new_entry: Any, index: Optional[int] = None) -> None:
        if index is None:
            index = self._size
        if index < 0 or index > self._size:
            raise IndexError
        if self._size >= self._capacity:
            self._resize()
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = new_entry
        self._size += 1

    def delete(self, index: int) -> Any:
        if self._size == 0 or index < 0 or index >= self._size:
            raise ValueError
        deleted_value = self._array[index]
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._array[self._size - 1] = None
        self._size -= 1
        if self._size > 0 and self._size <= self._capacity // 4:
            self._shrink()
        return deleted_value

    def find(self, target: Any) -> Optional[int]:
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

    def traverse(self, callback) -> None:
        for index in range(self._size):
            callback(self._array[index])

    def _resize(self) -> None:
        new_capacity = self._capacity * 2
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity
