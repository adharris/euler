

import click

from tools.primes import sieve_factors, calculate_totient
from operator import itemgetter

@click.command('70')
@click.option('--limit', '-l', type=int, default=10000000)
@click.option('--verbose', '-v', count=True)
def problem_070(limit,verbose):
    """Totient permutation.

    Euler's Totient function, φ(n) [sometimes called the phi function], is
    used to determine the number of positive numbers less than or equal to n
    which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
    all less than nine and relatively prime to nine, φ(9)=6.  
    The number 1 is considered to be relatively prime to every positive
    number, so φ(1)=1.
    
    Interestingly, φ(87109)=79180, and it can be seen that 87109 is a
    permutation of 79180.
    
    Find the value of n, 1 &lt; n &lt; 107, for which φ(n) is a permutation of
    n and the ratio n/φ(n) produces a minimum.
    
    """

    factors = sieve_factors(limit)
    totients = ((n, calculate_totient(n, f)) for n, f in factors.items())
    are_permutations = ((n, φ) for n, φ in totients if is_permutations(n, φ)) 
    ratios = ((n, n/φ) for n, φ in are_permutations)
    smallest = min(ratios, key=itemgetter(1))

    click.echo("{n}/φ({n}) = {n}/{φ} = {r}".format(
        n=smallest[0], 
        φ=calculate_totient(smallest[0], factors[smallest[0]]),
        r=smallest[1]))


def is_permutations(a, b):
    return a != b and sorted(str(a)) == sorted(str(b))