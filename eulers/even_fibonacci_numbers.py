# https://projecteuler.net/problem=2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four
# million, find the sum of the even-valued terms.

from itertools import count
from eulers.utils import fibonacci


def solution(limit: int) -> int:
    evens = []
    for i in count(start=1):
        value = fibonacci(i)
        if value > limit:
            break
        if value % 2 == 0:
            evens.append(value)

    return sum(evens)
