from .node import Node
from typing import Any

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def _search(self, value: Any):
        parent = None
        node = self._root
        while node is not None:
            if node._value == value:
                return node, parent
            elif value < node._value:
                parent = node
                node = node._left
            else: 
                parent = node
                node = node._right
        return None, parent

    def find_max_value(self, node: Node):
        parent = None
        current = node
        while current._right is not None:
            parent = current
            current = current._right
        return current, parent

    def insert(self, value: Any) -> None:
        node = self._root
        if node is None:
            self._root = Node(value)
        else:
            while node is not None:
                if value <= node._value:
                    if node._left is None:
                        new_node = Node(value)
                        node.set_left(new_node)
                        break
                    else:
                        node = node._left
                elif node._right is None:
                    new_node = Node(value)
                    node.set_right(new_node)
                    break
                else:
                    node = node._right

    def delete(self, value: Any) -> None:
        if self._root is None:
            raise ValueError
        node, parent = self._search(value)
        if node is None:
            raise ValueError
        if node._left is None and node._right is None:
            if parent is None:
                self._root = None
            elif value <= parent._value:
                parent.set_left(None)
            else:
                parent.set_right(None)
        elif node._left is None:
            if parent is None:
                self._root = node._right
                node._right._parent = None
            elif value <= parent._value:
                parent.set_left(node._right)
            else:
                parent.set_right(node._right)
        elif node._right is None:
            if parent is None:
                self._root = node._left
                node._left._parent = None
            elif parent._left is node:
                parent.set_left(node._left)
            else:
                parent.set_right(node._right)
        else:
            max_node, max_parent = self.find_max_value(node._left)
            node._value = max_node._value
            if max_parent is None:
                node._left = max_node._left
                if max_node._left is not None:
                    max_node._left._parent = node
            else:
                max_parent.set_right(max_node._left)