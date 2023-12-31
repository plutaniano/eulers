import pytest

from eulers.utils import is_anagram, is_prime, is_palindrome


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, False),
        (1, True),
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (21, False),
        (7757, True),
        (7758, False),
    ],
)
def test_is_prime(n: int, expected: bool) -> None:
    assert is_prime(n) == expected


def test_is_prime_raises_on_negative_numbers():
    with pytest.raises(TypeError):
        is_prime(-1)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("", "", True),
        (" ", " ", True),
        ("a", "a", True),
        ("é a", "a é", True),
        ("lucas", "sacul", True),
        ("a", "b", False),
        ("some_string", "", False),
        ("", "some_string", False),
        ("", " ", False),
    ],
)
def test_is_anagram(a: str, b: str, expected: bool) -> None:
    assert is_anagram(a, b) == expected


@pytest.mark.parametrize(
    "string,expected",
    [
        ("", True),
        (" ", True),
        ("a", True),
        ("ab", False),
        ("lucas", False),
        ("aba", True),
        (" a ", True),
        ("arara", True),
        ("abc", False),
        ("some_random_string", False),
    ],
)
def test_is_palindrome(string: str, expected: bool) -> None:
    assert is_palindrome(string) == expected
