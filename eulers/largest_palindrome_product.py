# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from eulers.utils import is_palindrome


def solution(digits: int) -> int:
    best = -1
    top, bottom = (10**digits) - 1, 10 ** (digits - 1)
    for i in range(top, bottom, -1):
        for j in range(top, bottom, -1):
            if is_palindrome(str(i * j)):
                best = max(i * j, best)
    return best
