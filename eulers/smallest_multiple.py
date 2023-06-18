# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers
# from 1 to 20?

from itertools import count


def solution(n: int):
    divisors = [20, 19, 18, 17, 16, 14, 13, 11]

    for i in count(start=2520, step=2520):
        if all(i % d == 0 for d in divisors):
            return i
