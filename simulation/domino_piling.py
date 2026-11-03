"""Domino Piling (Codeforces 50A).

Source: Codeforces, https://codeforces.com/problemset/problem/50/A

Place as many 2x1 dominoes as possible on an ``m x n`` board without
overlap. Return that count.

Approach:
    Every domino covers two cells and a board always admits a tiling that
    leaves at most one cell uncovered, so the answer is ``(m * n) // 2``.
    (Ported from the original 2023 Java solution.)

Complexity:
    Time  O(1).
    Space O(1).
"""

from __future__ import annotations


def max_dominoes(m: int, n: int) -> int:
    if m < 0 or n < 0:
        raise ValueError("board dimensions must be non-negative")
    return (m * n) // 2
