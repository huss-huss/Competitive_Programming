import pytest
from hypothesis import given
from hypothesis import strategies as st

from greedy.minimize_maximum_pair_sum import min_pair_sum
from greedy.minimum_increment_unique import min_increment_for_unique
from hashing.number_of_good_pairs import num_identical_pairs, num_identical_pairs_brute_force
from simulation.counting_valleys import counting_valleys
from simulation.domino_piling import max_dominoes
from simulation.fizz_buzz import fizz_buzz
from simulation.grading_students import grading_students
from two_pointers.container_with_most_water import max_area

# --- container with most water --------------------------------------------


@pytest.mark.parametrize(
    ("height", "expected"),
    [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1), ([4, 3, 2, 1, 4], 16), ([5], 0), ([], 0)],
)
def test_max_area(height, expected):
    assert max_area(height) == expected


@given(st.lists(st.integers(0, 1000), max_size=40))
def test_max_area_matches_brute_force(height):
    expected = max(
        (
            (j - i) * min(height[i], height[j])
            for i in range(len(height))
            for j in range(i + 1, len(height))
        ),
        default=0,
    )
    assert max_area(height) == expected


# --- minimize maximum pair sum --------------------------------------------


@pytest.mark.parametrize(
    ("nums", "expected"),
    [([3, 5, 2, 3], 7), ([3, 5, 4, 2, 4, 6], 8), ([1, 1], 2), ([], 0)],
)
def test_min_pair_sum(nums, expected):
    original = list(nums)
    assert min_pair_sum(nums) == expected
    assert nums == original


def _best_pairing(values):
    if not values:
        return 0
    first, rest = values[0], values[1:]
    return min(
        max(first + rest[i], _best_pairing(rest[:i] + rest[i + 1 :])) for i in range(len(rest))
    )


@given(
    st.integers(1, 4).flatmap(
        lambda n: st.lists(st.integers(0, 50), min_size=2 * n, max_size=2 * n)
    )
)
def test_min_pair_sum_is_optimal(nums):
    assert min_pair_sum(nums) == _best_pairing(nums)


# --- minimum increment for unique -----------------------------------------


@pytest.mark.parametrize(
    ("nums", "expected"),
    [([1, 2, 2], 1), ([3, 2, 1, 2, 1, 7], 6), ([], 0), ([5], 0), ([0, 0, 0], 3)],
)
def test_min_increment_for_unique(nums, expected):
    assert min_increment_for_unique(nums) == expected


@given(st.lists(st.integers(0, 50), max_size=40))
def test_min_increment_result_is_unique_and_minimal(nums):
    moves = min_increment_for_unique(nums)
    # Lower bound: the i-th smallest value must become at least
    # max(original, previous + 1); the greedy achieves exactly that sum.
    values, prev, expected = sorted(nums), -1, 0
    for v in values:
        prev = max(v, prev + 1)
        expected += prev - v
    assert moves == expected


# --- number of good pairs --------------------------------------------------


@pytest.mark.parametrize(
    ("nums", "expected"),
    [([1, 2, 3, 1, 1, 3], 4), ([1, 1, 1, 1], 6), ([1, 2, 3], 0), ([], 0)],
)
def test_num_identical_pairs(nums, expected):
    assert num_identical_pairs(nums) == expected
    assert num_identical_pairs_brute_force(nums) == expected


@given(st.lists(st.integers(0, 10), max_size=60))
def test_good_pairs_versions_agree(nums):
    assert num_identical_pairs(nums) == num_identical_pairs_brute_force(nums)


# --- fizz buzz -------------------------------------------------------------


def test_fizz_buzz_15():
    assert fizz_buzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz",
    ]  # fmt: skip


@pytest.mark.parametrize(("n", "expected"), [(0, []), (1, ["1"]), (3, ["1", "2", "Fizz"])])
def test_fizz_buzz_small(n, expected):
    assert fizz_buzz(n) == expected


# --- grading students ------------------------------------------------------


def test_grading_students_hackerrank_sample():
    assert grading_students([73, 67, 38, 33]) == [75, 67, 40, 33]


@pytest.mark.parametrize(
    ("grade", "expected"),
    [(37, 37), (38, 40), (39, 40), (40, 40), (41, 41), (42, 42), (43, 45), (100, 100), (0, 0)],
)
def test_grading_students_boundaries(grade, expected):
    assert grading_students([grade]) == [expected]


# --- counting valleys ------------------------------------------------------


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("UDDDUDUU", 1),
        ("DDUUDDUDUUUD", 2),
        ("UUDD", 0),
        ("", 0),
        ("DU", 1),
        ("DUDUDU", 3),
    ],
)
def test_counting_valleys(path, expected):
    assert counting_valleys(len(path), path) == expected


# --- domino piling ---------------------------------------------------------


@pytest.mark.parametrize(
    ("m", "n", "expected"), [(2, 4, 4), (3, 3, 4), (1, 1, 0), (16, 16, 128), (0, 5, 0)]
)
def test_max_dominoes(m, n, expected):
    assert max_dominoes(m, n) == expected


def test_max_dominoes_rejects_negative():
    with pytest.raises(ValueError):
        max_dominoes(-1, 2)
