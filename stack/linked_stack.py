import copy
from typing import Any

from linked_list.singly_linked.linked_list import SinglyLinkedList

class LinkedStack:
    def __init__(self):
        self._data = SinglyLinkedList()

    def is_empty(self) -> bool:
        return self._data.is_empty()

    def push(self, value: Any) -> None:
        self._data.insert_to_front(value)

    def pop(self) -> Any:
        if self.is_empty():
            raise ValueError
        return self._data.delete_from_front()

    def peek(self) -> Any:
        if self.is_empty():
            raise ValueError
        return self.get(0)

    def get(self, index: int) -> Any:
        if index < 0 or index >= len(self._data):
            raise IndexError
        return copy.deepcopy(self._data.get_by_index(index))

    def reverse(self) -> None:
        if self.is_empty():
            return
        current = self._data._head
        previous = None
        while current is not None:
            next_node = current.next()
            current.set_next(previous)
            previous = current
            current = next_node
        self._data._head = previous