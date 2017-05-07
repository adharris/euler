

import click

from fractions import Fraction
from itertools import product

@click.command('71')
@click.option('--limit', '-l', type=int, default=1000000)
@click.option('--numerator', '-n', type=int, default=3)
@click.option('--denominator', '-d', type=int, default=7)
@click.option('--verbose', '-v', count=True)
def problem_071(limit, numerator, denominator, verbose):
    """Ordered fractions.

    Consider the fraction, _n/d_, where _n_ and _d_ are positive integers. If
    _n_&lt;_d_ and HCF(_n,d_)=1, it is called a reduced proper fraction.
    
    If we list the set of reduced proper fractions for _d_ ≤ 8 in ascending
    order of size, we get:
    
    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, **2/5**, 3/7, 1/2, 4/7, 3/5, 5/8,
    2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
    
    It can be seen that 2/5 is the fraction immediately to the left of 3/7.
    
    By listing the set of reduced proper fractions for _d_ ≤ 1,000,000 in
    ascending order of size, find the numerator of the fraction immediately to
    the left of 3/7.
    
    """
    target = Fraction(numerator, denominator)
    fractions = (Fraction(int(n * target), n) for n in range(2, limit + 1))
    fractions = (f for f in fractions if f < target)
    closest = min(fractions, key=lambda f: target - f)
    click.echo(str(closest))
