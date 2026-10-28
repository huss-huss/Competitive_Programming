"""Minimize Maximum Pair Sum in Array (LeetCode 1877).

Source: LeetCode, https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

Split an even-length array into pairs so the largest pair sum is minimal;
return that sum.

Approach:
    Greedy: sort and pair the smallest with the largest, second smallest with
    second largest, and so on. Any other pairing puts a large value next to a
    larger partner (exchange argument).

Complexity:
    Time  O(n log n).
    Space O(n) for the sorted copy (the 2023 version sorted in place).
"""

from __future__ import annotations


def min_pair_sum(nums: list[int]) -> int:
    values = sorted(nums)
    n = len(values)
    return max((values[i] + values[n - i - 1] for i in range(n // 2)), default=0)
