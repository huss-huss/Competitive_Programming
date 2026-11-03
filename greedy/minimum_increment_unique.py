"""Minimum Increment to Make Array Unique (LeetCode 945).

Source: LeetCode, https://leetcode.com/problems/minimum-increment-to-make-array-unique/

One move increments any element by 1. Return the minimum moves needed so
all values are distinct.

Approach:
    Greedy after sorting: walk left to right and, whenever a value is not
    larger than its predecessor, raise it to ``predecessor + 1`` and add the
    difference to the move count.

Complexity:
    Time  O(n log n).
    Space O(n) for the sorted copy.
"""

from __future__ import annotations


def min_increment_for_unique(nums: list[int]) -> int:
    values = sorted(nums)
    moves = 0
    for i in range(1, len(values)):
        if values[i] <= values[i - 1]:
            target = values[i - 1] + 1
            moves += target - values[i]
            values[i] = target
    return moves
