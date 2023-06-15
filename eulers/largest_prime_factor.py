# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def solution(n: int) -> int:
    i = 2
    while i < math.sqrt(n):
        while n % i == 0:
            if n // i == 1:
                return n
            n = n // i
        i += 1
    return n
