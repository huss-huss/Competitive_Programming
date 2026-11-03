"""Insertion Sort - Part 1.

Source: HackerRank, https://www.hackerrank.com/challenges/insertionsort1/problem

The array is sorted except for its last element. Insert that element into
its correct place, printing the array after every shift and once more after
the final insertion.

Approach:
    Walk the last element left while it is smaller than its neighbour. Each
    step copies the neighbour one slot to the right (that intermediate state
    is recorded), then writes the element into the gap.

Complexity:
    Time  O(n^2) output size in the worst case (n lines of n numbers);
          O(n) element moves.
    Space O(1) extra besides the recorded lines.
"""

from __future__ import annotations


def _fmt(arr: list[int]) -> str:
    return " ".join(str(v) for v in arr)


def insertion_sort_steps(arr: list[int]) -> list[str]:
    """Insert the last element of ``arr`` in place; return every printed line."""
    lines: list[str] = []
    n = len(arr) - 1
    # 2023 version evaluated ``arr[n] < arr[n - 1]`` before ``n > 0``; harmless
    # in Python (arr[-1] is valid) but the bounds check now comes first.
    while n > 0 and arr[n] < arr[n - 1]:
        tmp = arr[n]
        arr[n] = arr[n - 1]
        lines.append(_fmt(arr))
        arr[n - 1] = tmp
        n -= 1
    lines.append(_fmt(arr))
    return lines


def insertion_sort(values: list[int]) -> list[int]:
    """Full insertion sort built from the single-insertion step. Returns a new list."""
    result: list[int] = []
    for v in values:
        result.append(v)
        insertion_sort_steps(result)
    return result
