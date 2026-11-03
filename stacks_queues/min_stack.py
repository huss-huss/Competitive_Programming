"""Min Stack (LeetCode 155).

Source: LeetCode, https://leetcode.com/problems/min-stack/

Design a stack supporting ``push``, ``pop``, ``top`` and ``get_min`` (LeetCode
name ``getMin``), all in O(1).

Approach:
    Keep a second stack where entry ``i`` is the minimum of the main stack's
    first ``i + 1`` items. Push ``min(val, current_min)``; pop both stacks
    together.

Complexity:
    Time  O(1) per operation.
    Space O(n) (two stacks).
"""

from __future__ import annotations


class MinStack:
    def __init__(self) -> None:
        self._stack: list[int] = []
        self._min_stack: list[int] = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._min_stack.append(min(val, self._min_stack[-1]) if self._min_stack else val)

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def get_min(self) -> int:
        return self._min_stack[-1]

    def __len__(self) -> int:
        return len(self._stack)
