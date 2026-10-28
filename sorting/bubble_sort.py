"""Sorting: Bubble Sort.

Source: HackerRank, https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

Sort an array with bubble sort, count the swaps performed, and report the
swap count together with the first and last element of the sorted array.

Approach:
    Classic bubble sort. After pass ``i`` the largest ``i + 1`` elements are in
    their final place, so the inner loop shrinks each pass. If a full pass
    makes no swap the array is already sorted and we stop early.

Complexity:
    Time  O(n^2) worst/average, O(n) best (already sorted, early exit).
    Space O(1) extra (sorts in place).
"""

from __future__ import annotations


def count_swaps(a: list[int]) -> int:
    """Sort ``a`` in place with bubble sort and return the number of swaps."""
    swaps, n = 0, len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                swapped = True
                swaps += 1
                a[j], a[j + 1] = a[j + 1], a[j]
        if not swapped:
            break
    return swaps


def bubble_sort(values: list[int]) -> list[int]:
    """Return a new sorted list (the input is left untouched)."""
    result = list(values)
    count_swaps(result)
    return result


def swap_report(a: list[int]) -> str:
    """Return the three output lines HackerRank expects for ``a``.

    ``a`` is sorted in place. Raises ``ValueError`` for an empty list because
    there is no first/last element to report.
    """
    if not a:
        raise ValueError("array must not be empty")
    swaps = count_swaps(a)
    return f"Array is sorted in {swaps} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}"
