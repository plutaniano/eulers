# https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for
# which, a^2 + b^2 = c^2.
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product a * b * c.


from typing import Generator
from math import sqrt


def squares() -> Generator[int, None, None]:
    i = 1
    while True:
        yield i * i
        i += 1


def solution(target: int) -> int:
    for a, a2 in enumerate(squares(), start=1):
        for b, b2 in enumerate(squares(), start=1):
            c = sqrt(a2 + b2)
            if a + b + c > target:
                break
            if not c.is_integer():
                continue
            if a + b + c == target:
                return int(a * b * c)
