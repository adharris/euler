

import click

from collections import defaultdict
from functools import reduce
from operator import mul, itemgetter


@click.command('69')
@click.option('--limit', '-l', type=int, default=1000000)
@click.option('--verbose', '-v', count=True)
def problem_069(limit,verbose):
    """Totient maximum.

    Euler's Totient function, φ(_n_) [sometimes called the phi function], is
    used to determine the number of numbers less than _n_ which are relatively
    prime to _n_. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
    and relatively prime to nine, φ(9)=6.
    
    **_n_** | **Relatively Prime** | **φ(_n_)** | **_n_/φ(_n_)**  
    ---|---|---|---  
    2 | 1 | 1 | 2  
    3 | 1,2 | 2 | 1.5  
    4 | 1,3 | 2 | 2  
    5 | 1,2,3,4 | 4 | 1.25  
    6 | 1,5 | 2 | 3  
    7 | 1,2,3,4,5,6 | 6 | 1.1666...  
    8 | 1,3,5,7 | 4 | 2  
    9 | 1,2,4,5,7,8 | 6 | 1.5  
    10 | 1,3,7,9 | 4 | 2.5  
      
    It can be seen that _n_=6 produces a maximum _n_/φ(_n_) for _n_ ≤ 10.
    
    Find the value of _n_ ≤ 1,000,000 for which _n_/φ(_n_) is a maximum.
    
    """
    factors = sieve_factors(limit)
    
    totient = ((n, calculate_totient(n, f)) for n, f in factors.items())
    ratio = ((n, n / φ) for n, φ in totient)
    highest_ratio = max(ratio, key=itemgetter(1))
    click.echo("{0}/φ({0})={1}".format(*highest_ratio))


def calculate_totient(number, factors):

    # Euler's Product formula:
    # φ(n) = n(1 - 1/p1)(1 - 1/p2)...(1-1/pr)
    # where p1..pr are unique factors of n

    return int(reduce(mul, ((1 - (1 / p)) for p in factors), number))


def sieve_factors(limit):
    factors = defaultdict(tuple)

    for i in range(2, limit // 2 + 1):

        # If we haven't seen factors if i, it is prime
        if len(factors[i]) == 0:
            factors[i] = ()
        
            # Normally we can loop starting a n^2, but since we are collecting
            # factors, we need to start at n
            for j in range(i, limit + 1, i):
                factors[j] += (i, )

    return factors

