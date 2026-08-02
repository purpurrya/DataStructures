from collections.abc import Callable
from decimal import Decimal
from math import floor, sqrt
from typing import Any

from linked_list.singly_linked.linked_list import SinglyLinkedList


class HashTable:
    __A__ = Decimal((sqrt(5) - 1) / 2)

    def __init__(self, buckets: int, extract_key: Callable[[Any], Any] = hash) -> None:
        self._m: int = buckets
        self._data: list[SinglyLinkedList] = [SinglyLinkedList() for _ in range(buckets)]
        self._extract_key: Callable[[Any], Any] = extract_key

    def hash(self, key: Any) -> int:
        return floor(self._m * (Decimal(key) * HashTable.__A__ % 1))

    def insert(self, value: Any) -> None:
        index: int = self.hash(self._extract_key(value))
        self._data[index].insert_in_front(value)

    def _search(self, value: Any) -> Any | None:
        index: int = self.hash(self._extract_key(value))
        value_matches_key = lambda x: self._extract_key(x) == self._extract_key(value)
        return self._data[index].search(value_matches_key)

    def delete(self, value: Any) -> None:
        index: int = self.hash(self._extract_key(value))
        self._data[index].delete(value)