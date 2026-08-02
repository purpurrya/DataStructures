from typing import Any

class Node:
    def __init__(self, value: Any, left=None, right=None, parent=None):
        self._value = value
        self._left = left
        self._right = right
        self._parent = parent

    def set_left(self, left):
        self._left = left
        if left is not None:
            left._parent = self

    def set_right(self, right):
        self._right = right
        if right is not None:
            right._parent = self

    def set_parent(self, parent):
        self._parent = parent