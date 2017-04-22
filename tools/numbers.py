
from math import log

def digit(number, n):
    """Return the digit in the nth significant place"""
    return (number // 10 ** n) % 10


def digit_count(n):
    """Returns the numer of digits in n"""
    return int(log(n, 10)) + 1


def iter_digits(n):
    """Returns an iterable of the digits in n, starting with the least significant"""
    return (digit(n, i) for i in range(digit_count(n)))


def digits_to_number(digits):
    """Create a number from an interable of digits with least significant first"""
    return sum(d * 10 ** i for i, d in enumerate(digits))
    