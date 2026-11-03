"""Counting Valleys.

Source: HackerRank, https://www.hackerrank.com/challenges/counting-valleys/problem

A hike is a string of ``U`` (up) and ``D`` (down) steps starting and ending
at sea level. A valley is a maximal run below sea level. Count the valleys.

Approach:
    Track the altitude. Stepping down to -1 means a valley started; coming
    back up to 0 after that closes it.

Complexity:
    Time  O(n).
    Space O(1).
"""

from __future__ import annotations


def counting_valleys(steps: int, path: str) -> int:
    """Return the number of valleys in ``path``.

    ``steps`` is the HackerRank-provided length of ``path``; it is not needed
    by the algorithm and only kept for signature compatibility.
    """
    altitude = 0
    in_valley = False
    valleys = 0
    for step in path:
        altitude += 1 if step == "U" else -1
        if altitude == -1:
            in_valley = True
        if in_valley and altitude == 0:
            valleys += 1
            in_valley = False
    return valleys
