from typing import Any

from ..queue.circular_queue import CircularQueue
from ..stack.linked_stack import LinkedStack
from .vertex import Vertex


class Graph:
    def __init__(self) -> None:
        self._adj: dict[Any, Vertex] = {}

    def _get_vertex(self, key: Any) -> Vertex:
        if key not in self._adj:
            raise ValueError
        return self._adj[key]

    def insert_vertex(self, key: Any) -> None:
        if key in self._adj:
            raise ValueError
        self._adj[key] = Vertex(key)

    def insert_edge(self, key1: Any, key2: Any) -> None:
        v1 = self._get_vertex(key1)
        v2 = self._get_vertex(key2)
        v1.add_edge_to(v2)

    def delete_vertex(self, key: Any) -> None:
        v = self._get_vertex(key)
        for x in self._adj.values():
            if x != v and x.has_edge_to(v):
                x.remove_edge_to(v)
        del self._adj[key]

    def bfs(self, start_vertex: Any, target_vertex: Any) -> list[Any] | None:
        distance: dict[Any, float] = {v: float('inf') for v in self._adj}
        predecessor: dict[Any, Any | None] = {v: None for v in self._adj}
        queue = CircularQueue(len(self._adj))
        queue.enqueue(start_vertex)
        distance[start_vertex] = 0

        while not queue.is_empty():
            u = queue.dequeue()
            if u == target_vertex:
                return self._reconstruct_path(predecessor, target_vertex)
            for v in self._get_vertex(u).outgoing_edges():
                if distance[v] == float('inf'):
                    distance[v] = distance[u] + 1
                    predecessor[v] = u
                    queue.enqueue(v)
        return None

    def _reconstruct_path(self, pred: dict[Any, Any | None], target: Any) -> list[Any]:
        path: list[Any] = []
        while target is not None:
            path.append(target)
            target = pred[target]
        return path[::-1]

    def dfs(self, start_vertex: Any) -> tuple[bool, dict[Any, str]]:
        color: dict[Any, str] = {v: 'white' for v in self._adj}
        acyclic: bool = True
        stack = LinkedStack()
        stack.push((False, start_vertex))

        while not stack.is_empty():
            mark_as_black, v = stack.pop()
            col = color.get(v, 'white')

            if mark_as_black:
                color[v] = 'black'
            elif col == 'grey':
                acyclic = False
            elif col == 'white':
                color[v] = 'grey'
                stack.push((True, v))
                for w in self._get_vertex(v).outgoing_edges():
                    stack.push((False, w))

        return acyclic, color

    def vertex_count(self) -> int:
        return len(self._adj)