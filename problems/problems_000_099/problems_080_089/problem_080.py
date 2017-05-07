
import click

from decimal import Decimal, Context
from math import sqrt

@click.command('80')
@click.option('--decimals', '-d', type=int, default=100)
@click.option('--limit', '-l', type=int, default=100)
@click.option('--verbose', '-v', count=True)
def problem_080(decimals, limit, verbose):
    """Square root digital expansion.

    It is well known that if the square root of a natural number is not an
    integer, then it is irrational. The decimal expansion of such square roots
    is infinite without any repeating pattern at all.
    
    The square root of two is 1.41421356237309504880..., and the digital sum
    of the first one hundred decimal digits is 475.
    
    For the first one hundred natural numbers, find the total of the digital
    sums of the first one hundred decimal digits for all the irrational square
    roots.
    
    """

    sums = (sum_of_sqrt_digits(n, decimals) for n in range(limit))
    click.echo(sum(sums))

    
def sum_of_sqrt_digits(value, digits):
    
    if int(sqrt(value))**2 == value:
        return 0

    precision = digits + 2
    root = Decimal(value).sqrt(Context(precision))
    return sum(root.as_tuple().digits[:digits])

def sqrt_with_n_decimals(value, n):
    precision = n + 20
    return Decimal(value).sqrt(Context(precision))


def get_decimals(value):
    as_tuple = value.as_tuple()
    return as_tuple.digits
