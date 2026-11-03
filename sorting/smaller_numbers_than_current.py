"""How Many Numbers Are Smaller Than the Current Number (LeetCode 1365).

Source: LeetCode, https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

For each ``nums[i]`` count how many values in ``nums`` are strictly smaller.

Approach:
    Sort a copy. The first index at which a value appears in the sorted list
    equals the number of strictly smaller values. Record that first index per
    value in a dict, then look each original value up.

Complexity:
    Time  O(n log n).
    Space O(n).
"""

from __future__ import annotations


def smaller_numbers_than_current(nums: list[int]) -> list[int]:
    """Return ``[count of values < nums[i] for each i]``."""
    first_index: dict[int, int] = {}
    for i, val in enumerate(sorted(nums)):
        if val not in first_index:
            first_index[val] = i
    return [first_index[val] for val in nums]
