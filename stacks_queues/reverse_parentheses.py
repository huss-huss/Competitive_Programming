"""Reverse Substrings Between Each Pair of Parentheses (LeetCode 1190).

Source: LeetCode, https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

Reverse the strings inside each pair of matching parentheses, innermost
first, and return the result without any brackets.

Approach:
    Push characters on a stack. On ``)`` pop back to the matching ``(``; the
    popped characters come out reversed, so push them straight back.

Complexity:
    Time  O(n^2) worst case (deeply nested input re-reverses inner text).
    Space O(n).
"""

from __future__ import annotations


def reverse_parentheses(s: str) -> str:
    stack: list[str] = []
    for ch in s:
        if ch != ")":
            stack.append(ch)
            continue
        reversed_chunk: list[str] = []
        while stack[-1] != "(":
            reversed_chunk.append(stack.pop())
        stack.pop()  # discard "("
        stack.extend(reversed_chunk)
    return "".join(stack)
