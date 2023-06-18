from typing import Generator
from collections import Counter
from functools import lru_cache


def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 0


def primes() -> Generator[int, None, None]:
    yield 2
    n = 1
    while True:
        n += 2
        if is_prime(n):
            yield n


def is_anagram(a: str, b: str) -> bool:
    return Counter(a) == Counter(b)


def is_palindrome(string: str) -> bool:
    return string == string[::-1]


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
