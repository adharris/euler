

import click

from tools.primes import PrimeCache
from tools.memoization import memoize
from itertools import count

@click.command('47')
@click.option('--verbose', '-v', count=True)
def problem_047(verbose):
    """Distinct primes factors.

    The first two consecutive numbers to have two distinct prime factors are:
    
    14 = 2 × 7  
    15 = 3 × 5
    
    The first three consecutive numbers to have three distinct prime factors
    are:
    
    644 = 2² × 7 × 23  
    645 = 3 × 5 × 43  
    646 = 2 × 17 × 19.
    
    Find the first four consecutive integers to have four distinct prime
    factors each. What is the first of these numbers?
    
    """

    cache = PrimeCache(100000)
    numbers = count(5)
    factors_in_a_row = (n for n in numbers if last_n_had_n_factors(cache, n, 4))
    click.echo(next(factors_in_a_row))



def last_n_had_n_factors(primes, number, n):
    for i in range(n):
        if count_unique_factors(primes, number - i) != n:
            return False
    return True 


@memoize
def count_unique_factors(primes, number):
    factors = set(primes.factor(number))
    return len(factors)