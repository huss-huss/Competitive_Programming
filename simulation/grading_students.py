"""Grading Students.

Source: HackerRank, https://www.hackerrank.com/challenges/grading/problem

Round each grade up to the next multiple of 5 when the difference is less
than 3. Grades below 38 are failing and are never rounded.

Approach:
    For each grade ``g >= 38`` compute ``r = g % 5``; if ``r >= 3`` the next
    multiple of 5 is ``5 - r`` away (1 or 2), so round up.

Complexity:
    Time  O(n).
    Space O(n) for the output.
"""

from __future__ import annotations


def grading_students(grades: list[int]) -> list[int]:
    new_grades: list[int] = []
    for grade in grades:
        remainder = grade % 5
        if grade >= 38 and remainder >= 3:
            new_grades.append(grade + (5 - remainder))
        else:
            new_grades.append(grade)
    return new_grades
