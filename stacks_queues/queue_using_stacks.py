"""Implement Queue using Stacks (LeetCode 232).

Source: LeetCode, https://leetcode.com/problems/implement-queue-using-stacks/

Implement a FIFO queue using only stack operations (push to top, pop/peek
from top, size, is empty).

Approach:
    Two stacks. ``push`` appends to the inbox. ``pop``/``peek`` read from the
    outbox; when it is empty, move every inbox item over, which reverses
    their order so the oldest item ends up on top.

    Fix: the 2023 version used one list and removed ``stack[0]``, i.e. a
    queue operation the problem forbids, costing O(n) per pop.

Complexity:
    Time  O(1) amortized per operation (each item moves at most once).
    Space O(n).
"""

from __future__ import annotations


class MyQueue:
    def __init__(self) -> None:
        self._inbox: list[int] = []
        self._outbox: list[int] = []

    def push(self, x: int) -> None:
        self._inbox.append(x)

    def _shift(self) -> None:
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())

    def pop(self) -> int:
        self._shift()
        return self._outbox.pop()

    def peek(self) -> int:
        self._shift()
        return self._outbox[-1]

    def empty(self) -> bool:
        return not self._inbox and not self._outbox
