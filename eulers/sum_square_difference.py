# https://projecteuler.net/problem=6
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + 3^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + 3 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


def solution(n: int) -> int:
    numbers = list(range(1, n + 1))

    sum_of_squares = sum(i**2 for i in numbers)
    square_of_the_sum = sum(numbers) ** 2

    return abs(sum_of_squares - square_of_the_sum)
