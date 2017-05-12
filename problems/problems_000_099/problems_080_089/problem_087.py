

import click

from math import sqrt
from tools.primes import sieve_of_eratosthenes
from bisect import bisect_left

@click.command('87')
@click.option('--limit', '-l', type=int, default=50000000)
@click.option('--verbose', '-v', count=True)
def problem_087(limit,verbose):
    """Prime power triples.

    The smallest number expressible as the sum of a prime square, prime cube,
    and prime fourth power is 28. In fact, there are exactly four numbers
    below fifty that can be expressed in such a way:
    
    28 = 2^2 + 2^3 + 2^4  
    33 = 3^2 + 2^3 + 2^4  
    49 = 5^2 + 2^3 + 2^4  
    47 = 2^2 + 3^3 + 2^4
    
    How many numbers below fifty million can be expressed as the sum of a
    prime square, prime cube, and prime fourth power?
    
    """

    # The Biggest prime needed will be P where
    # Limit > P^2 + 2^3 + 2^4
    # sqrt(Limit - 24) > P

    prime_bound = int(sqrt(limit - 24)) + 1
    primes = sieve_of_eratosthenes(prime_bound)

    print(len(set((genrate_triples(primes, limit)))))


def genrate_triples(primes, limit):
    with click.progressbar(primes) as bar:
        for prime_1 in power_range(bar, 2, limit):
            remaining_1 = limit - prime_1**2
            for prime_2 in power_range(primes, 3, remaining_1):
                remaining_2 = remaining_1 - prime_2**3
                for prime_3 in power_range(primes, 4, remaining_2):
                    yield prime_1**2 + prime_2**3 + prime_3 ** 4


def power_range(primes, power, limit):
    for prime in primes:
        value = prime**power
        if value > limit:
            return
        yield prime