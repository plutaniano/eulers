def test_001():
    from eulers.multiples_of_3_or_5 import solution

    assert solution(1000) == 233168


def test_002():
    from eulers.even_fibonacci_numbers import solution

    assert solution(4_000_000) == 4613732


def test_003():
    from eulers.largest_prime_factor import solution

    assert solution(600851475143) == 6857


def test_004():
    from eulers.largest_palindrome_product import solution

    assert solution(3) == 906609


def test_005():
    from eulers.smallest_multiple import solution

    assert solution(20) == 232792560
