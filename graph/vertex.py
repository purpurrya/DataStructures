from typing import Any

from linked_list.singly_linked.linked_list import SinglyLinkedList


class Vertex:
    def __init__(self, key: Any) -> None:
        self.id = key
        self._adj_list: SinglyLinkedList[Any] = SinglyLinkedList()

    def has_edge_to(self, destination_vertex: Any) -> bool:
        return self._adj_list.search(destination_vertex) is not None

    def add_edge_to(self, destination_vertex: Any) -> None:
        if self.has_edge_to(destination_vertex):
            raise ValueError
        self._adj_list.insert_in_front(destination_vertex)

    def remove_edge_to(self, destination_vertex: Any) -> None:
        self._adj_list.delete(destination_vertex)

    def outgoing_edges(self) -> SinglyLinkedList[Any]:
        return self._adj_list