class Node:
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node
        self._prev = None

    def data(self):
        return self._data
    
    def next(self):
        return self._next
    
    def has_next(self):
        return self._next is not None
    
    def append(self, next_node): 
        self._next = next_node
        if next_node is not None:
            next_node._prev = self

    def prev(self):
        return self._prev
    
    def has_prev(self):
        return self._prev is not None
    
    def prepend(self, prev_node):
        self._prev = prev_node
        if prev_node is not None:
            prev_node._next = self