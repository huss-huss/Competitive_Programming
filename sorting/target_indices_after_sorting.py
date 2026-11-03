"""Find Target Indices After Sorting Array (LeetCode 2089).

Source: LeetCode, https://leetcode.com/problems/find-target-indices-after-sorting-array/

Return the indices where ``target`` appears once ``nums`` is sorted in
non-decreasing order.

Approach:
    Sort, then collect every index whose value equals ``target``. (The 2023
    version left a debug ``print(nums)`` and sorted the caller's list in
    place; both removed.)

Complexity:
    Time  O(n log n).
    Space O(n) for the sorted copy.
"""

from __future__ import annotations


def target_indices(nums: list[int], target: int) -> list[int]:
    """Return sorted-order indices of ``target`` in ``nums``."""
    sorted_nums = sorted(nums)
    return [i for i, val in enumerate(sorted_nums) if val == target]
