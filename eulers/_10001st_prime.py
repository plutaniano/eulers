# https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that
# the 6th prime is 13.
# What is the 10001st prime number?


from eulers.utils import primes


def solution(n: int) -> int:
    gen = primes()

    for _ in range(n - 1):
        next(gen)
    return next(gen)
