"""Selection Sort.

Source: GeeksforGeeks, https://www.geeksforgeeks.org/problems/selection-sort/1

Sort an array in ascending order with selection sort by implementing
``select(arr, i)`` (place the minimum of ``arr[i:]`` at index ``i``) and
``selection_sort(arr, n)``.

Approach:
    For each position ``i``, scan the unsorted suffix and swap any smaller
    element into ``arr[i]``. After the scan ``arr[i]`` holds the suffix
    minimum. (This swap-as-you-go variant does more swaps than the textbook
    version that remembers the min index, but the same comparisons.)

Complexity:
    Time  O(n^2).
    Space O(1) extra (in place).
"""

from __future__ import annotations


def select(arr: list[int], i: int) -> int:
    """Move the minimum of ``arr[i:]`` to ``arr[i]`` and return it."""
    for j in range(i, len(arr)):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
    return arr[i]


def selection_sort(arr: list[int], n: int | None = None) -> None:
    """Sort the first ``n`` positions of ``arr`` in place (default: whole list)."""
    if n is None:
        n = len(arr)
    for i in range(n):
        select(arr, i)
