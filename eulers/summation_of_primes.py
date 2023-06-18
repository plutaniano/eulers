# https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


from eulers.utils import primes


def solution(upper_bound: int) -> int:
    total = 0
    for prime in primes():
        if prime > upper_bound:
            break
        total += prime
    return total
