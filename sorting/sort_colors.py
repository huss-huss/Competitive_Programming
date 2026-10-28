"""Sort Colors (LeetCode 75).

Source: LeetCode, https://leetcode.com/problems/sort-colors/

Sort a list containing only 0, 1 and 2 in place, without using the library
sort.

Approach:
    The 2023 version simply called ``nums.sort()``, which the problem asks
    you not to do. It is kept as ``sort_colors_builtin`` for comparison.
    ``sort_colors`` is the one-pass Dutch national flag partition: ``low``
    marks the end of the 0s, ``high`` the start of the 2s, and ``mid`` scans
    the unknown region between them.

Complexity:
    sort_colors:          Time O(n), Space O(1).
    sort_colors_builtin:  Time O(n log n), Space O(n) worst case (Timsort).
"""

from __future__ import annotations


def sort_colors(nums: list[int]) -> None:
    """Sort ``nums`` (values 0, 1, 2) in place in a single pass."""
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


def sort_colors_builtin(nums: list[int]) -> None:
    """Original 2023 solution: delegate to ``list.sort``."""
    nums.sort()
