import copy
from typing import Any, List, Optional, Callable

class Heap:
    def __init__(self, elements: Optional[List[Any]] = None, 
                 element_priority: Callable[[Any], Any] = lambda x: x):
        self._priority = element_priority
        self._elements = []
        
        if elements is not None:
            self._elements = elements.copy()
            if len(self._elements) > 0:
                self._heapify()
    
    def __len__(self) -> int:
        return len(self._elements)
    
    def __getitem__(self, index: int) -> Any:
        return self._elements[index]
    
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    def _has_higher_priority(self, index1: int, index2: int) -> bool:
        return self._priority(self._elements[index1]) < self._priority(self._elements[index2])
    
    def _parent_index(self, index: int) -> int:
        return (index - 1) // 2
    
    def _left_child_index(self, index: int) -> int:
        return 2 * index + 1
    
    def _swap(self, index1: int, index2: int) -> None:
        self._elements[index1], self._elements[index2] = self._elements[index2], self._elements[index1]
    
    def insert(self, value: Any) -> None:
        self._elements.append(value)
        self._bubble_up(len(self._elements) - 1)
    
    def _bubble_up(self, index: int) -> None:
        while index > 0:
            parent = self._parent_index(index)
            if self._has_higher_priority(index, parent):
                self._swap(index, parent)
                index = parent
            else:
                break
    
    def pop(self) -> Any:
        if self.is_empty():
            raise ValueError
        
        result = self._elements[0]
        
        if len(self._elements) == 1:
            self._elements.pop()
        else:
            self._elements[0] = self._elements.pop()
            self._push_down(0)
        
        return result
    
    def peek(self) -> Any:
        if self.is_empty():
            raise ValueError
        return copy.deepcopy(self._elements[0])
    
    def _push_down(self, index: int) -> None:
        while True:
            child = self._highest_priority_child_index(index)
            if child is None:
                break
            if self._has_higher_priority(child, index):
                self._swap(index, child)
                index = child
            else:
                break
    
    def _highest_priority_child_index(self, index: int) -> Optional[int]:
        left = self._left_child_index(index)
        if left >= len(self._elements):
            return None
        
        right = left + 1
        if right >= len(self._elements):
            return left
        
        if self._has_higher_priority(left, right):
            return left
        return right
    
    def _heapify(self) -> None:
        for index in range(len(self._elements) // 2 - 1, -1, -1):
            self._push_down(index)
    
    def clear(self) -> None:
        self._elements.clear()
    
    def __repr__(self) -> str:
        return f"Heap({self._elements})"


def k_largest_elements(arr: List[Any], k: int) -> List[Any]:
    if k <= 0:
        return []
    if k >= len(arr):
        return sorted(arr, reverse=True)[:k]
    
    heap = Heap()
    
    for element in arr:
        if len(heap) < k:
            heap.insert(element)
        elif element > heap.peek():
            heap.pop()
            heap.insert(element)
    
    result = []
    while not heap.is_empty():
        result.append(heap.pop())
    
    return result[::-1]