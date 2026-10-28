"""Find the Kth Largest Integer in the Array (LeetCode 1985).

Source: LeetCode, https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

Numbers are given as strings without leading zeros (they may exceed 64-bit
range). Return the k-th largest one as a string; duplicates count separately.

Approach:
    Convert to ``int`` (Python ints are arbitrary precision), sort ascending,
    and take index ``-k``.

Complexity:
    Time  O(n log n) comparisons (each on up to m-digit numbers, plus O(n*m)
          parsing).
    Space O(n) for the converted, sorted list.
"""

from __future__ import annotations


def kth_largest_number(nums: list[str], k: int) -> str:
    """Return the ``k``-th largest value in ``nums`` (1-indexed)."""
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    sorted_nums = sorted(int(val) for val in nums)
    return str(sorted_nums[-k])
