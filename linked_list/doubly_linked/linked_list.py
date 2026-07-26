from collections.abc import Callable
from typing import Any

from linked_list.node import Node


class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def __len__(self) -> int:
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.next()
        return count
    
    def is_empty(self) -> bool:
        return self._head is None

    def insert_to_front(self, data: Any) -> None:
        if self.is_empty():
            self._head = self._tail = Node(data)
        else:
            old_head = self._head
            self._head = Node(data, old_head)
            old_head.prepend(self._head)

    def insert_to_back(self, data: Any) -> None:
        if self.is_empty():
            self._head = self._tail = Node(data)
        else:
            old_tail = self._tail
            self._tail = Node(data)
            old_tail.append(self._tail)

    def insert_after(self, data: Any, node: Node) -> None:
        if self.is_empty():
            self._tail = self._head = Node(data)
            return
        else:
            new_node = Node(data, node.next())
            node.append(new_node)

            if new_node.next() is not None:
                new_node.next().prepend(new_node)
            
            if node == self._tail:
                self._tail = new_node

    def search_from_front(self, target: Any) -> Node | None:
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None
    
    def search_from_back(self, target: Any) -> Node | None:
        current = self._tail
        while current is not None:
            if current.data() == target:
                return current
            current = current.prev()
        return None
    
    def delete(self, target: Any) -> None:
        node = self.search_from_front(target)
        if node is None:
            raise ValueError
        if node.prev() is None:
            self._head = node.next()
            if self._head is None:
                self._tail = None
            else:
                self._head.prepend(None)
        elif node.next() is None:
            self._tail = node.prev()
            self._tail.append(None)
        else:
            node.prev().append(node.next())
            node.next().prepend(node.prev())
    
    def delete_from_front(self) -> Any:
        if self.is_empty():
            raise ValueError
        
        deleted_data = self._head.data()
        self._head = self._head.next()
        if self._head is None:
            self._tail = None
        else:
            self._head.prepend(None)
        return deleted_data

    def delete_from_back(self) -> Any:
        if self.is_empty():
            raise ValueError
        
        deleted_data = self._tail.data()
        self._tail = self._tail.prev()
        if self._tail is None:
            self._head = None
        else:
            self._tail.append(None)
        return deleted_data
    
    def map(self, function: Callable[[Any], Any]) -> 'DoubleLinkedList':
        result = DoubleLinkedList()
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