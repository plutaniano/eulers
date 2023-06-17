from collections import Counter


def is_prime(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 0


def is_anagram(a: str, b: str) -> bool:
    return Counter(a) == Counter(b)