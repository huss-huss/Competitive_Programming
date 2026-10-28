"""Evaluate Reverse Polish Notation (LeetCode 150).

Source: LeetCode, https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate an arithmetic expression in postfix notation with ``+ - * /``.
Division truncates toward zero.

Approach:
    Push operands on a stack; on an operator pop the right operand, then the
    left operand, apply the operator and push the result.

    Fix: the 2023 version divided with ``int(float(b) / a)``. That is correct
    inside LeetCode's 32-bit limits but loses precision once operands exceed
    2**53 (e.g. ``(10**17 + 1) / 1``). Truncating integer division is now done
    exactly with ``//`` on absolute values.

Complexity:
    Time  O(n) tokens.
    Space O(n) stack.
"""

from __future__ import annotations

OPERATORS = frozenset("+-*/")


def _div_trunc(a: int, b: int) -> int:
    """Integer division truncating toward zero (C/Java semantics)."""
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b > 0) else -q


def eval_rpn(tokens: list[str]) -> int:
    """Evaluate ``tokens`` and return the integer result."""
    stack: list[int] = []
    for token in tokens:
        if token in OPERATORS:
            right, left = stack.pop(), stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                stack.append(_div_trunc(left, right))
        else:
            stack.append(int(token))
    if len(stack) != 1:
        raise ValueError("malformed RPN expression")
    return stack[0]
