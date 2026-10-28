"""Sorting the Sentence (LeetCode 1859).

Source: LeetCode, https://leetcode.com/problems/sorting-the-sentence/

Each word of a shuffled sentence has its 1-indexed position (1-9) appended.
Rebuild the original sentence.

Approach:
    Split into words; the last character of each word is its position, so
    place the word (minus that digit) directly into a results slot.

Complexity:
    Time  O(n) in the length of the sentence.
    Space O(n).
"""

from __future__ import annotations


def sort_sentence(s: str) -> str:
    """Return the original sentence from its shuffled, position-tagged form."""
    words = s.split()
    results = [""] * len(words)
    for word in words:
        results[int(word[-1]) - 1] = word[:-1]
    return " ".join(results)
