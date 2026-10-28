"""Number of Good Pairs (LeetCode 1512).

Source: LeetCode, https://leetcode.com/problems/number-of-good-pairs/

Count pairs ``(i, j)`` with ``i < j`` and ``nums[i] == nums[j]``.

Approach:
    ``num_identical_pairs_brute_force`` is the original 2023 double loop.
    ``num_identical_pairs`` counts in one pass: each new occurrence of a
    value forms a good pair with every earlier occurrence.

Complexity:
    num_identical_pairs:             Time O(n),   Space O(n).
    num_identical_pairs_brute_force: Time O(n^2), Space O(1).
"""

from __future__ import annotations

from collections import defaultdict


def num_identical_pairs(nums: list[int]) -> int:
    seen: defaultdict[int, int] = defaultdict(int)
    pairs = 0
    for val in nums:
        pairs += seen[val]
        seen[val] += 1
    return pairs


def num_identical_pairs_brute_force(nums: list[int]) -> int:
    pairs = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                pairs += 1
    return pairs
