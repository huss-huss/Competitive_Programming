"""Validate Stack Sequences (LeetCode 946).

Source: LeetCode, https://leetcode.com/problems/validate-stack-sequences/

Given ``pushed`` and ``popped`` (permutations of distinct values), decide
whether they could result from push/pop operations on an empty stack.

Approach:
    Simulate: push each value, then greedily pop while the top matches the
    next expected popped value. Valid iff the stack ends empty.

Complexity:
    Time  O(n) (each value pushed and popped at most once).
    Space O(n).
"""

from __future__ import annotations


def validate_stack_sequences(pushed: list[int], popped: list[int]) -> bool:
    stack: list[int] = []
    i = 0
    for val in pushed:
        stack.append(val)
        while stack and i < len(popped) and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return not stack and i == len(popped)
