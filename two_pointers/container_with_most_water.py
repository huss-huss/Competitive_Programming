"""Container With Most Water (LeetCode 11).

Source: LeetCode, https://leetcode.com/problems/container-with-most-water/

Pick two vertical lines that, with the x-axis, hold the most water.

Approach:
    Two pointers at both ends. The area is limited by the shorter line, and
    moving the taller one inward can never increase it, so always move the
    shorter pointer.

Complexity:
    Time  O(n).
    Space O(1).
"""

from __future__ import annotations


def max_area(height: list[int]) -> int:
    best = 0
    left, right = 0, len(height) - 1
    while left < right:
        best = max(best, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
