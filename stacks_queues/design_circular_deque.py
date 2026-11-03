"""Design Circular Deque (LeetCode 641).

Source: LeetCode, https://leetcode.com/problems/design-circular-deque/

Design a double-ended queue with fixed capacity ``k``. Insert/delete return
``True`` on success and ``False`` when full/empty; ``get_front``/``get_rear``
return ``-1`` when empty. (LeetCode uses camelCase names such as
``insertFront``; this file was named "Design-Circular-Queue" in 2023 but it
implements the deque problem.)

Approach:
    A plain Python list bounded by ``k``: front operations work at index 0,
    rear operations at the end.

Complexity:
    Time  O(1) for rear operations and reads; O(k) for ``insert_front`` and
          ``delete_front`` (list shifts). A ring buffer would make all O(1).
    Space O(k).
"""

from __future__ import annotations


class MyCircularDeque:
    def __init__(self, k: int) -> None:
        self._deque: list[int] = []
        self._k = k

    def insert_front(self, value: int) -> bool:
        if len(self._deque) < self._k:
            self._deque.insert(0, value)
            return True
        return False

    def insert_last(self, value: int) -> bool:
        if len(self._deque) < self._k:
            self._deque.append(value)
            return True
        return False

    def delete_front(self) -> bool:
        if self._deque:
            self._deque.pop(0)
            return True
        return False

    def delete_last(self) -> bool:
        if self._deque:
            self._deque.pop()
            return True
        return False

    def get_front(self) -> int:
        return self._deque[0] if self._deque else -1

    def get_rear(self) -> int:
        return self._deque[-1] if self._deque else -1

    def is_empty(self) -> bool:
        return not self._deque

    def is_full(self) -> bool:
        return len(self._deque) == self._k
