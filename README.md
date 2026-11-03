# Algorithms & Data Structures in Python

[![CI](https://github.com/huss-huss/Competitive_Programming/actions/workflows/ci.yml/badge.svg)](https://github.com/huss-huss/Competitive_Programming/actions/workflows/ci.yml)

Solutions to classic problems from LeetCode, HackerRank, GeeksforGeeks and
Codeforces, organised by topic. Every solution is a small importable module
with a docstring (problem, approach, time/space complexity), type hints and
tests.

The solutions were first written in 2023 while practising competitive
programming. In 2026 the repo was refactored into topic packages, bugs and
shortcuts in the original code were fixed (each fix is noted in the module
docstring), and a pytest + hypothesis test suite and CI were added.

## Index

| Problem | Topic | Difficulty | Time | Space | File |
| --- | --- | --- | --- | --- | --- |
| Sorting: Bubble Sort (HackerRank) | Sorting | Easy | O(n²) | O(1) | [sorting/bubble_sort.py](sorting/bubble_sort.py) |
| Counting Sort 1 (HackerRank) | Sorting | Easy | O(n + k) | O(k) | [sorting/counting_sort.py](sorting/counting_sort.py) |
| Insertion Sort - Part 1 (HackerRank) | Sorting | Easy | O(n) moves | O(1) | [sorting/insertion_sort.py](sorting/insertion_sort.py) |
| Selection Sort (GeeksforGeeks) | Sorting | Easy | O(n²) | O(1) | [sorting/selection_sort.py](sorting/selection_sort.py) |
| 75. Sort Colors (LeetCode) | Sorting / two pointers | Medium | O(n) | O(1) | [sorting/sort_colors.py](sorting/sort_colors.py) |
| 1985. Find the Kth Largest Integer in the Array (LeetCode) | Sorting | Medium | O(n log n) | O(n) | [sorting/kth_largest_integer.py](sorting/kth_largest_integer.py) |
| 2089. Find Target Indices After Sorting Array (LeetCode) | Sorting | Easy | O(n log n) | O(n) | [sorting/target_indices_after_sorting.py](sorting/target_indices_after_sorting.py) |
| 1365. How Many Numbers Are Smaller Than the Current Number (LeetCode) | Sorting / hashing | Easy | O(n log n) | O(n) | [sorting/smaller_numbers_than_current.py](sorting/smaller_numbers_than_current.py) |
| 1859. Sorting the Sentence (LeetCode) | Sorting / strings | Easy | O(n) | O(n) | [sorting/sorting_the_sentence.py](sorting/sorting_the_sentence.py) |
| 150. Evaluate Reverse Polish Notation (LeetCode) | Stack | Medium | O(n) | O(n) | [stacks_queues/evaluate_rpn.py](stacks_queues/evaluate_rpn.py) |
| 155. Min Stack (LeetCode) | Stack / design | Medium | O(1) per op | O(n) | [stacks_queues/min_stack.py](stacks_queues/min_stack.py) |
| 232. Implement Queue using Stacks (LeetCode) | Queue / design | Easy | O(1) amortized | O(n) | [stacks_queues/queue_using_stacks.py](stacks_queues/queue_using_stacks.py) |
| 641. Design Circular Deque (LeetCode) | Deque / design | Medium | O(1) rear, O(k) front | O(k) | [stacks_queues/design_circular_deque.py](stacks_queues/design_circular_deque.py) |
| 946. Validate Stack Sequences (LeetCode) | Stack / simulation | Medium | O(n) | O(n) | [stacks_queues/validate_stack_sequences.py](stacks_queues/validate_stack_sequences.py) |
| 1190. Reverse Substrings Between Each Pair of Parentheses (LeetCode) | Stack / strings | Medium | O(n²) | O(n) | [stacks_queues/reverse_parentheses.py](stacks_queues/reverse_parentheses.py) |
| 11. Container With Most Water (LeetCode) | Two pointers | Medium | O(n) | O(1) | [two_pointers/container_with_most_water.py](two_pointers/container_with_most_water.py) |
| 1877. Minimize Maximum Pair Sum in Array (LeetCode) | Greedy / sorting | Medium | O(n log n) | O(n) | [greedy/minimize_maximum_pair_sum.py](greedy/minimize_maximum_pair_sum.py) |
| 945. Minimum Increment to Make Array Unique (LeetCode) | Greedy / sorting | Medium | O(n log n) | O(n) | [greedy/minimum_increment_unique.py](greedy/minimum_increment_unique.py) |
| 1512. Number of Good Pairs (LeetCode) | Hashing / counting | Easy | O(n) | O(n) | [hashing/number_of_good_pairs.py](hashing/number_of_good_pairs.py) |
| 412. Fizz Buzz (LeetCode) | Simulation | Easy | O(n) | O(1) extra | [simulation/fizz_buzz.py](simulation/fizz_buzz.py) |
| Grading Students (HackerRank) | Simulation | Easy | O(n) | O(n) | [simulation/grading_students.py](simulation/grading_students.py) |
| Counting Valleys (HackerRank) | Simulation | Easy | O(n) | O(1) | [simulation/counting_valleys.py](simulation/counting_valleys.py) |
| 50A. Domino Piling (Codeforces) | Math | 800 | O(1) | O(1) | [simulation/domino_piling.py](simulation/domino_piling.py) |

Difficulty is the platform's label (Codeforces shows the problem rating).
Where a module has two versions (e.g. Sort Colors, Number of Good Pairs), the
table lists the primary one; the docstring covers both.

## Layout

```
sorting/         sorting algorithms and sort-based problems
stacks_queues/   stack, queue and deque problems and designs
two_pointers/    two-pointer techniques
greedy/          greedy problems
hashing/         counting / hash map problems
simulation/      direct simulation and math
tests/           pytest + hypothesis tests, one file per topic group
```

## Running the tests

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install pytest hypothesis ruff

pytest              # run all tests
ruff check .        # lint
ruff format --check .
```

Tests combine the problem's sample cases and edge cases with
[hypothesis](https://hypothesis.readthedocs.io/) property tests: sorting
functions are checked against `sorted()`, and the min stack, queue and
circular deque are checked against simple reference models over random
operation sequences. CI runs lint and tests on Python 3.11 and 3.12.
