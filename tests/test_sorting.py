import pytest
from hypothesis import given
from hypothesis import strategies as st

from sorting.bubble_sort import bubble_sort, count_swaps, swap_report
from sorting.counting_sort import count_frequencies, counting_sort
from sorting.insertion_sort import insertion_sort, insertion_sort_steps
from sorting.kth_largest_integer import kth_largest_number
from sorting.selection_sort import select, selection_sort
from sorting.smaller_numbers_than_current import smaller_numbers_than_current
from sorting.sort_colors import sort_colors, sort_colors_builtin
from sorting.sorting_the_sentence import sort_sentence
from sorting.target_indices_after_sorting import target_indices

int_lists = st.lists(st.integers(min_value=-1000, max_value=1000), max_size=60)


# --- bubble sort -----------------------------------------------------------


def test_bubble_sort_hackerrank_sample():
    assert swap_report([6, 4, 1]) == (
        "Array is sorted in 3 swaps.\nFirst Element: 1\nLast Element: 6"
    )


def test_bubble_sort_already_sorted_has_zero_swaps():
    a = [1, 2, 3]
    assert count_swaps(a) == 0
    assert a == [1, 2, 3]


@pytest.mark.parametrize("a", [[], [7]])
def test_bubble_sort_trivial_inputs(a):
    assert count_swaps(list(a)) == 0


def test_swap_report_rejects_empty():
    with pytest.raises(ValueError):
        swap_report([])


def _inversions(a):
    return sum(1 for i in range(len(a)) for j in range(i + 1, len(a)) if a[i] > a[j])


@given(int_lists)
def test_bubble_sort_matches_sorted(values):
    assert bubble_sort(values) == sorted(values)


@given(int_lists)
def test_bubble_swaps_equal_inversions(values):
    a = list(values)
    assert count_swaps(a) == _inversions(values)


# --- counting sort ---------------------------------------------------------


def test_counting_frequencies_basic():
    freq = count_frequencies([1, 1, 3, 2, 1])
    assert len(freq) == 100
    assert freq[:4] == [0, 3, 1, 1]
    assert sum(freq) == 5


def test_counting_frequencies_empty():
    assert count_frequencies([]) == [0] * 100


@pytest.mark.parametrize("bad", [-1, 100])
def test_counting_frequencies_out_of_range(bad):
    with pytest.raises(ValueError):
        count_frequencies([bad])


@given(st.lists(st.integers(min_value=0, max_value=99), max_size=200))
def test_counting_sort_matches_sorted(values):
    assert counting_sort(values) == sorted(values)


# --- insertion sort --------------------------------------------------------


def test_insertion_sort_steps_hackerrank_sample():
    arr = [2, 4, 6, 8, 3]
    assert insertion_sort_steps(arr) == [
        "2 4 6 8 8",
        "2 4 6 6 8",
        "2 4 4 6 8",
        "2 3 4 6 8",
    ]
    assert arr == [2, 3, 4, 6, 8]


def test_insertion_sort_steps_new_minimum_reaches_front():
    arr = [2, 4, 1]
    assert insertion_sort_steps(arr) == ["2 4 4", "2 2 4", "1 2 4"]


def test_insertion_sort_steps_already_in_place():
    assert insertion_sort_steps([1, 2, 3]) == ["1 2 3"]
    assert insertion_sort_steps([5]) == ["5"]


@given(int_lists)
def test_insertion_sort_matches_sorted(values):
    assert insertion_sort(values) == sorted(values)


# --- selection sort --------------------------------------------------------


def test_selection_sort_gfg_examples():
    a = [4, 1, 3, 9, 7]
    selection_sort(a, 5)
    assert a == [1, 3, 4, 7, 9]
    b = list(range(10, 0, -1))
    selection_sort(b)
    assert b == list(range(1, 11))


def test_select_returns_minimum_of_suffix():
    a = [5, 9, 2, 7]
    assert select(a, 1) == 2
    assert a[:2] == [5, 2]


@given(int_lists)
def test_selection_sort_matches_sorted(values):
    a = list(values)
    selection_sort(a)
    assert a == sorted(values)


# --- sort colors -----------------------------------------------------------


@pytest.mark.parametrize(
    ("nums", "expected"),
    [([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]), ([2, 0, 1], [0, 1, 2]), ([], []), ([1], [1])],
)
def test_sort_colors_examples(nums, expected):
    a = list(nums)
    sort_colors(a)
    assert a == expected
    b = list(nums)
    sort_colors_builtin(b)
    assert b == expected


@given(st.lists(st.sampled_from([0, 1, 2]), max_size=100))
def test_sort_colors_matches_sorted(values):
    a = list(values)
    sort_colors(a)
    assert a == sorted(values)


# --- kth largest -----------------------------------------------------------


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        (["3", "6", "7", "10"], 4, "3"),
        (["2", "21", "12", "1"], 3, "2"),
        (["0", "0"], 2, "0"),
        (["123456789012345678901234567890", "9"], 1, "123456789012345678901234567890"),
    ],
)
def test_kth_largest_number(nums, k, expected):
    assert kth_largest_number(nums, k) == expected


@pytest.mark.parametrize("k", [0, 3])
def test_kth_largest_number_invalid_k(k):
    with pytest.raises(ValueError):
        kth_largest_number(["1", "2"], k)


# --- target indices --------------------------------------------------------


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([1, 2, 5, 2, 3], 2, [1, 2]),
        ([1, 2, 5, 2, 3], 3, [3]),
        ([1, 2, 5, 2, 3], 5, [4]),
        ([1, 2, 5, 2, 3], 4, []),
        ([], 1, []),
    ],
)
def test_target_indices(nums, target, expected):
    original = list(nums)
    assert target_indices(nums, target) == expected
    assert nums == original  # input not mutated


# --- smaller numbers than current -----------------------------------------


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
        ([6, 5, 4, 8], [2, 1, 0, 3]),
        ([7, 7, 7, 7], [0, 0, 0, 0]),
        ([], []),
    ],
)
def test_smaller_numbers_than_current(nums, expected):
    assert smaller_numbers_than_current(nums) == expected


@given(int_lists)
def test_smaller_numbers_matches_brute_force(values):
    expected = [sum(1 for w in values if w < v) for v in values]
    assert smaller_numbers_than_current(values) == expected


# --- sorting the sentence --------------------------------------------------


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("is2 sentence4 This1 a3", "This is a sentence"),
        ("Myself2 Me1 I4 and3", "Me Myself and I"),
        ("word1", "word"),
    ],
)
def test_sort_sentence(s, expected):
    assert sort_sentence(s) == expected
