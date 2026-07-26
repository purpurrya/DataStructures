from collections.abc import Callable
from typing import Any

from linked_list.node import Node


class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self) -> bool:
        return self._head is None

    def insert_to_front(self, data: Any) -> None:
        if self.is_empty():
            self._head = Node(data)
            self._tail = self._head
            self._head.append(self._tail)
            self._tail.prepend(self._head)
        else:
            old_head = self._head
            self._head = Node(data, old_head, self._tail)
            self._tail.append(self._head)
            old_head.prepend(self._head)

    def insert_to_back(self, data: Any) -> None:
        if self.is_empty():
            self._head = Node(data)
            self._tail = self._head
            self._head.append(self._tail)
            self._tail.prepend(self._head)
        else:
            new_node = Node(data, self._head, self._tail)
            self._tail.append(new_node)
            self._tail = new_node
            self._head.prepend(self._tail)

    def insert_after(self, data: Any, node: Node) -> None:
        if self.is_empty():
            self._tail = self._head = Node(data)
            return
        else:
            new_node = Node(data, node.next(), node)
            node.append(new_node)
            new_node.next().prepend(new_node)
            
            if node == self._tail:
                self._tail = new_node

    def search_from_front(self, target: Any) -> Node | None:
        if self.is_empty():
            return None
        current = self._head
        while True:
            if current.data() == target:
                return current
            current = current.next()
            if current == self._head:
                break
        return None
    
    def search_from_back(self, target: Any) -> Node | None:
        if self.is_empty():
            return None
        current = self._tail
        while True:
            if current.data() == target:
                return current
            current = current.prev()
            if current == self._tail:
                break
        return None
    
    def delete(self, target: Any) -> None:
        node = self.search_from_front(target)
        if node is None:
            raise ValueError
        if node == self._head and node == self._tail:
            self._head = None
            self._tail = None
        elif node == self._head:
            self._head = node.next()
            self._tail.append(self._head)
            self._head.prepend(self._tail)
        elif node == self._tail:
            self._tail = node.prev()
            self._tail.append(self._head)
            self._head.prepend(self._tail)
        else:
            node.prev().append(node.next())
            node.next().prepend(node.prev())
    
    def delete_from_front(self) -> Any:
        if self.is_empty():
            raise ValueError
        
        deleted_data = self._head.data()
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next()
            self._tail.append(self._head)
            self._head.prepend(self._tail)
        return deleted_data

    def delete_from_back(self) -> Any:
        if self.is_empty():
            raise ValueError
        
        deleted_data = self._tail.data()
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.prev()
            self._tail.append(self._head)
            self._head.prepend(self._tail)
        return deleted_data
    
    def map(self, function: Callable[[Any], Any]) -> 'DoubleLinkedList':
        result = DoubleLinkedList()
        if self.is_empty():
            return result
        current = self._head
        while True:
            result.insert_to_back(function(current.data()))
            current = current.next()
            if current == self._head:
                break
        return result
    
    def apply(self, function: Callable[[Any], Any]) -> None:
        if self.is_empty():
            return
        current = self._head
        while True:
            current._data = function(current.data())
            current = current.next()
            if current == self._head:
                break