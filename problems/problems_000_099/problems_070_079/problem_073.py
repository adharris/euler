

import click
from fractions import Fraction

from tools.primes import sieve_factors


@click.command('73')
@click.option('--limit', '-l', type=int, default=12000)
@click.option('--lower', type=Fraction, default=Fraction(1, 3))
@click.option('--upper', type=Fraction, default=Fraction(1, 2))
@click.option('--verbose', '-v', count=True)
def problem_073(limit, lower, upper, verbose):
    """Counting fractions in a range.

    Consider the fraction, _n/d_, where _n_ and _d_ are positive integers. If
    _n_&lt;_d_ and HCF(_n,d_)=1, it is called a reduced proper fraction.
    
    If we list the set of reduced proper fractions for _d_ ≤ 8 in ascending
    order of size, we get:
    
    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, **3/8, 2/5, 3/7**, 1/2, 4/7, 3/5, 5/8,
    2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
    
    It can be seen that there are 3 fractions between 1/3 and 1/2.
    
    How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
    proper fractions for _d_ ≤ 12,000?
    
    """

    factors = sieve_factors(limit)
    factors = {n: set(f) for n, f in factors.items()}

    denominators = click.progressbar(range(2, limit + 1))
    with denominators:
        fractions = [
            (n, d)
            for d in denominators
            for n in find_numerator_range(lower, upper, d)
            if are_coprime(factors, n, d)]
    
    click.echo(len(fractions))


def are_coprime(factors, a, b):
    return a == 1 or b == 1 or len(factors[a] & factors[b]) == 0


def find_numerator_range(lower, upper, denominator):
    return range(
        find_lower_numerator(lower, denominator),
        find_upper_numerator(upper, denominator) + 1)


def find_lower_numerator(target, denominator):
    if target.denominator == denominator:
        return target.numerator + 1
    return int(denominator * target) + 1


def find_upper_numerator(target, denominator):
    if target.denominator == denominator:
        return target.numerator - 1
    return int(denominator * target)