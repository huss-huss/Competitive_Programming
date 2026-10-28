"""Fizz Buzz (LeetCode 412).

Source: LeetCode, https://leetcode.com/problems/fizz-buzz/

Return strings for ``1..n``: "FizzBuzz" for multiples of 15, "Fizz" for
multiples of 3, "Buzz" for multiples of 5, otherwise the number itself.

Approach:
    Straight iteration, checking divisibility by both 3 and 5 first.

Complexity:
    Time  O(n).
    Space O(n) for the output (O(1) extra).
"""

from __future__ import annotations


def fizz_buzz(n: int) -> list[str]:
    answer: list[str] = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer
