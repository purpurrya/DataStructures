from collections.abc import Callable

from linked_list.node import Node
from linked_list.singly_linked.linked_list import SinglyLinkedList


class CycledSinglyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self._tail = None

    def __len__(self) -> int:
        if self.is_empty():
            return 0
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.next()
            if current == self._head:
                break
        return count

    def insert_to_back(self, data) -> None:
        if self.is_empty():
            self._head = Node(data)
            self._tail = self._head
            self._tail.append(self._head)
        else:
            new_node = Node(data)
            self._tail.append(new_node)
            self._tail = new_node
            self._tail.append(self._head)

    def insert_to_front(self, data) -> None:
        if self.is_empty():
            self._head = Node(data)
            self._tail = self._head
            self._tail.append(self._head)
        else:
            old_head = self._head
            self._head = Node(data, old_head)
            self._tail.append(self._head)

    def search(self, target) -> Node | None:
        if self.is_empty():
            return None
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
            if current == self._head:
                break
        return None

    def delete(self, target) -> None:
        if self.is_empty():
            raise ValueError
        
        current = self._head
        previous = self._tail
        
        while current is not None:
            if current.data() == target:
                if current == self._head and current == self._tail:
                    self._head = None
                    self._tail = None
                elif current == self._head:
                    self._head = current.next()
                    self._tail.append(self._head)
                elif current == self._tail:
                    self._tail = previous
                    self._tail.append(self._head)
                else:
                    previous.append(current.next())
                return
            previous = current
            current = current.next()
            if current == self._head:
                break
        raise ValueError

    def delete_from_front(self):
        if self.is_empty():
            raise ValueError
        
        deleted_data = self._head.data()
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next()
            self._tail.append(self._head)
        return deleted_data

    def map(self, function: Callable) -> 'CycledSinglyLinkedList':
        result = CycledSinglyLinkedList()
        if self.is_empty():
            return result
        current = self._head
        while current is not None:
            result.insert_to_back(function(current.data()))
            current = current.next()
            if current == self._head:
                break
        return result

    def apply(self, function: Callable) -> None:
        if self.is_empty():
            return
        current = self._head
        while current is not None:
            current._data = function(current.data())
            current = current.next()
            if current == self._head:
                break