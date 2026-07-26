from collections.abc import Callable
from typing import Any

from linked_list.node import Node


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def __len__(self) -> int:
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.next()
        return count
    
    def is_empty(self) -> bool:
        return self._head is None

    def insert_to_back(self, data: Any) -> None:
        current = self._head
        if current is None:
            self._head = Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(Node(data))

    def insert_to_front(self, data: Any) -> None:
        old_head = self._head
        self._head = Node(data, old_head)

    def search(self, target: Any) -> Node | None:
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None
    
    def delete(self, target: Any) -> None:
        current = self._head 
        previous = None
        while current is not None:
            if current.data() == target:
                if previous is None:
                    self._head = current.next()
                else:
                    previous.append(current.next())
                return 
            previous = current
            current = current.next()
        raise ValueError
    
    def delete_from_front(self) -> Any:
        if not self.is_empty():
            deleted_data = self._head.data()
            self._head = self._head.next()
            return deleted_data
        raise ValueError
    
    def map(self, function: Callable[[Any], Any]) -> 'SinglyLinkedList':
        result = SinglyLinkedList()
        current = self._head 
        while current is not None:
            result.insert_to_back(function(current.data()))
            current = current.next()
        return result
    
    def apply(self, function: Callable[[Any], Any]) -> None:
        current = self._head
        while current is not None:
            current._data = function(current.data())
            current = current.next()