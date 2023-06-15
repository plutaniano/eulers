# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers
# from 1 to 20?

from itertools import count


def solution(n: int):
    divisors = list(range(n, 0, -1))

    for i in range(1, int(10e9), max(divisors)):
        if any(i % div != 0 for div in divisors):
            break
        else:
            return i
