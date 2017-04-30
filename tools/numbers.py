
from math import log, sqrt



def digit(number, n):
    """Return the digit in the nth significant place"""
    return (number // 10 ** n) % 10


def digit_count(n):
    """Returns the numer of digits in n"""
    return len(str(n))


def set_digit(number, d, v):
    base = 10**d
    return number - base * digit(number, d) + base * v


def iter_digits(n):
    """Returns an iterable of the digits in n, starting with the least significant"""
    return (digit(n, i) for i in range(digit_count(n)))


def digits_to_number(digits):
    """Create a number from an interable of digits with least significant first"""
    return sum(d * 10 ** i for i, d in enumerate(digits))


def is_perfect_square(n):
    return int(sqrt(n)) == sqrt(n)


def sqrt_continuted_fraction(number):
    """https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion"""

    if int(sqrt(number)) == sqrt(number):
        return ContinuedFraction(int(sqrt(number)), ())

    m = 0
    d = 1
    a = [int(sqrt(number)) ]

    while a[-1] != a[0] * 2:
        m = d * a[-1] -  m
        d = (number - m**2) // d
        next_a = int((a[0] + m) / d)
        a.append(next_a)

    return tuple(a)
