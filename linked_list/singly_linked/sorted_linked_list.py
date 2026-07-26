from collections.abc import Callable
from typing import Any

from linked_list.node import Node


class SinglyLinkedSortedList:
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

    def insert(self, new_data: Any) -> None:
        current = self._head
        previous = None
        while current is not None:
            if current.data() >= new_data:
                if previous is None:
                    self.insert_to_front(new_data)
                else:
                    previous.append(Node(new_data, current))
                return 
            previous = current
            current = current.next() 
        if previous is None:
            self._head = Node(new_data)
        else:
            previous.append(Node(new_data))

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
    
    def map(self, function: Callable[[Any], Any]) -> 'SinglyLinkedSortedList':
        result = SinglyLinkedSortedList()
        current = self._head 
        while current is not None:
            result.insert(function(current.data()))
            current = current.next()
        return result
    
    def apply(self, function: Callable[[Any], Any]) -> None:
        current = self._head
        while current is not None:
            current._data = function(current.data())
            current = current.next()