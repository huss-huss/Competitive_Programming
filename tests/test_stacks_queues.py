from collections import deque

import pytest
from hypothesis import given
from hypothesis import strategies as st

from stacks_queues.design_circular_deque import MyCircularDeque
from stacks_queues.evaluate_rpn import eval_rpn
from stacks_queues.min_stack import MinStack
from stacks_queues.queue_using_stacks import MyQueue
from stacks_queues.reverse_parentheses import reverse_parentheses
from stacks_queues.validate_stack_sequences import validate_stack_sequences

# --- evaluate RPN ----------------------------------------------------------


@pytest.mark.parametrize(
    ("tokens", "expected"),
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        (["7"], 7),
        (["-7", "2", "/"], -3),  # truncates toward zero, not floor
        (["7", "-2", "/"], -3),
        (["3", "5", "-"], -2),
    ],
)
def test_eval_rpn(tokens, expected):
    assert eval_rpn(tokens) == expected


def test_eval_rpn_large_operands_are_exact():
    big = 10**17 + 1
    assert eval_rpn([str(big), "1", "/"]) == big


def test_eval_rpn_malformed():
    with pytest.raises(ValueError):
        eval_rpn(["1", "2"])


@given(st.integers(-(10**30), 10**30), st.integers(-(10**30), 10**30).filter(bool))
def test_eval_rpn_division_truncates_toward_zero(a, b):
    q = eval_rpn([str(a), str(b), "/"])
    assert abs(q) == abs(a) // abs(b)
    assert q == 0 or (q > 0) == ((a > 0) == (b > 0))


# --- min stack -------------------------------------------------------------


def test_min_stack_leetcode_example():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.get_min() == -3
    s.pop()
    assert s.top() == 0
    assert s.get_min() == -2


def test_min_stack_duplicate_minimums():
    s = MinStack()
    for v in (1, 1, 2):
        s.push(v)
    s.pop()
    s.pop()
    assert s.get_min() == 1


ops = st.lists(st.one_of(st.integers(-100, 100), st.none()), max_size=80)


@given(ops)
def test_min_stack_matches_model(operations):
    s, model = MinStack(), []
    for op in operations:
        if op is None:
            if model:
                s.pop()
                model.pop()
        else:
            s.push(op)
            model.append(op)
        assert len(s) == len(model)
        if model:
            assert s.top() == model[-1]
            assert s.get_min() == min(model)


# --- queue using stacks ----------------------------------------------------


def test_queue_leetcode_example():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert not q.empty()
    assert q.pop() == 2
    assert q.empty()


def test_queue_pop_empty_raises():
    with pytest.raises(IndexError):
        MyQueue().pop()


@given(ops)
def test_queue_matches_deque(operations):
    q, model = MyQueue(), deque()
    for op in operations:
        if op is None:
            if model:
                assert q.pop() == model.popleft()
        else:
            q.push(op)
            model.append(op)
        assert q.empty() == (not model)
        if model:
            assert q.peek() == model[0]


# --- circular deque --------------------------------------------------------


def test_circular_deque_leetcode_example():
    d = MyCircularDeque(3)
    assert d.insert_last(1)
    assert d.insert_last(2)
    assert d.insert_front(3)
    assert not d.insert_front(4)
    assert d.get_rear() == 2
    assert d.is_full()
    assert d.delete_last()
    assert d.insert_front(4)
    assert d.get_front() == 4


def test_circular_deque_empty_behaviour():
    d = MyCircularDeque(1)
    assert d.is_empty()
    assert d.get_front() == -1
    assert d.get_rear() == -1
    assert not d.delete_front()
    assert not d.delete_last()


deque_ops = st.lists(
    st.tuples(
        st.sampled_from(["insert_front", "insert_last", "delete_front", "delete_last"]),
        st.integers(0, 1000),
    ),
    max_size=80,
)


@given(st.integers(1, 8), deque_ops)
def test_circular_deque_matches_bounded_model(k, operations):
    d, model = MyCircularDeque(k), deque()
    for name, value in operations:
        if name == "insert_front":
            ok = len(model) < k
            if ok:
                model.appendleft(value)
            assert d.insert_front(value) == ok
        elif name == "insert_last":
            ok = len(model) < k
            if ok:
                model.append(value)
            assert d.insert_last(value) == ok
        elif name == "delete_front":
            ok = bool(model)
            if ok:
                model.popleft()
            assert d.delete_front() == ok
        else:
            ok = bool(model)
            if ok:
                model.pop()
            assert d.delete_last() == ok
        assert d.get_front() == (model[0] if model else -1)
        assert d.get_rear() == (model[-1] if model else -1)
        assert d.is_empty() == (not model)
        assert d.is_full() == (len(model) == k)


# --- validate stack sequences ---------------------------------------------


@pytest.mark.parametrize(
    ("pushed", "popped", "expected"),
    [
        ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
        ([], [], True),
        ([1], [1], True),
        ([1, 2], [1], False),
        ([1], [1, 2], False),
    ],
)
def test_validate_stack_sequences(pushed, popped, expected):
    assert validate_stack_sequences(pushed, popped) is expected


@given(st.permutations(list(range(8))), st.lists(st.booleans(), min_size=16, max_size=16))
def test_validate_accepts_any_simulated_sequence(pushed, choices):
    # Build a real popped sequence by randomly interleaving pushes and pops.
    stack, popped, it = [], [], iter(pushed)
    remaining = len(pushed)
    for do_pop in choices:
        if do_pop and stack:
            popped.append(stack.pop())
        elif remaining:
            stack.append(next(it))
            remaining -= 1
    for v in it:
        stack.append(v)
    popped.extend(reversed(stack))
    assert validate_stack_sequences(list(pushed), popped)


# --- reverse parentheses ---------------------------------------------------


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("(abcd)", "dcba"),
        ("(u(love)i)", "iloveu"),
        ("(ed(et(oc))el)", "leetcode"),
        ("a(bcdefghijkl(mno)p)q", "apmnolkjihgfedcbq"),
        ("", ""),
        ("abc", "abc"),
        ("()", ""),
    ],
)
def test_reverse_parentheses(s, expected):
    assert reverse_parentheses(s) == expected
