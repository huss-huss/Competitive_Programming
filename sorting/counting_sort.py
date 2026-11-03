"""Counting Sort 1.

Source: HackerRank, https://www.hackerrank.com/challenges/countingsort1/problem

Given integers in the range ``[0, 100)``, return a frequency array of length
100 where index ``v`` holds how many times ``v`` occurs.

Approach:
    One pass over the input incrementing ``count[value]``. The frequency
    array is the first half of counting sort; ``counting_sort`` expands it
    back into a sorted list.

Complexity:
    Time  O(n + k) with k = 100 buckets.
    Space O(k) for the frequency array (O(n + k) for the sorted output).
"""

from __future__ import annotations

from collections.abc import Iterable

MAX_VALUE = 100


def count_frequencies(arr: Iterable[int], size: int = MAX_VALUE) -> list[int]:
    """Return a list of ``size`` counts, where ``count[v]`` is the frequency of ``v``.

    Raises ``ValueError`` if a value falls outside ``[0, size)``.
    """
    count = [0] * size
    for val in arr:
        if not 0 <= val < size:
            raise ValueError(f"value {val} outside range [0, {size})")
        count[val] += 1
    return count


def counting_sort(arr: Iterable[int], size: int = MAX_VALUE) -> list[int]:
    """Return the values of ``arr`` in ascending order using counting sort."""
    result: list[int] = []
    for value, freq in enumerate(count_frequencies(arr, size)):
        result.extend([value] * freq)
    return result
