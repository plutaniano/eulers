def test_001():
    from eulers.multiples_of_3_or_5 import solution

    assert solution(1_000) == 233_168


def test_002():
    from eulers.even_fibonacci_numbers import solution

    assert solution(4_000_000) == 4_613_732


def test_003():
    from eulers.largest_prime_factor import solution

    assert solution(600_851_475_143) == 6_857


def test_004():
    from eulers.largest_palindrome_product import solution

    assert solution(3) == 906_609


def test_005():
    from eulers.smallest_multiple import solution

    assert solution(20) == 232_792_560
