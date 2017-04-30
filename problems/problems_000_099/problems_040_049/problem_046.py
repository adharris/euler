

import click
from tools.primes import PrimeCache
from math import sqrt
from itertools import count

@click.command('46')
@click.option('--verbose', '-v', count=True)
def problem_046(verbose):
    """Goldbach's other conjecture.

    It was proposed by Christian Goldbach that every odd composite number can
    be written as the sum of a prime and twice a square.
    
    9 = 7 + 2×1^2  
    15 = 7 + 2×2^2  
    21 = 3 + 2×3^2  
    25 = 7 + 2×3^2  
    27 = 19 + 2×2^2  
    33 = 31 + 2×1^2
    
    It turns out that the conjecture was false.
    
    What is the smallest odd composite that cannot be written as the sum of a
    prime and twice a square?
    
    """

    primes = PrimeCache(10000)
    odd_composites = (n for n in count(3, 2) if not primes.is_prime(n))
    factored = (find_prime_and_square(primes, n) for n in odd_composites)

    try:
        for item in factored:
            if verbose:
                click.echo("{} + 2×{}^2 = {}".format(*item))
    except ValueError as e:
        click.echo(e)


def find_prime_and_square(primes, odd_composite):
    primes.ensure_factors_for(odd_composite)
    smaller_primes = (p for p in primes.primes if p < odd_composite)
    for prime in smaller_primes:
        remainder = odd_composite - prime
        base = sqrt(remainder / 2)
        if int(base) == base:
            return prime, int(base), odd_composite
    raise ValueError(odd_composite)