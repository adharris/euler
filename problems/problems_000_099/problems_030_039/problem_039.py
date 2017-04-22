

import click

from math import sqrt, ceil, floor
from tools.primes import sieve_of_eratosthenes, factor_with_primes
from tools.memoization import memoize
from collections import Counter
from itertools import count


@click.command('39')
@click.option('--limit', '-l', type=int, default=1000)
@click.option('--verbose', '-v', count=True)
def problem_039(limit,verbose):
    """Integer right triangles.

    If _p_ is the perimeter of a right angle triangle with integral length
    sides, {_a_,_b_,_c_}, there are exactly three solutions for _p_ = 120.
    
    {20,48,52}, {24,45,51}, {30,40,50}
    
    For which value of _p_ ≤ 1000, is the number of solutions maximised?
    
    """

    # We could enumerate all triples that sum to < 1000, but there are a bunch
    # of em.  Instead, we can use euclids method to generate primitive triples
    # When we bound m and n of euclids method using the target perimiter, we
    # get much fewer values to try. We do have to check if they are coprime,
    # but this is fast with memoized prime table.  This method runs in reasonble
    # time for perimeters up to 10e5.

    # Euclid's method:
    # a = k(m^2 - n^2)
    # b = k(2mn)
    # c = k(m^2 + n^2)
    # For coprime m and n and not both odd and any integer k
    # a + b + c = m^2 - n^2 + 2mn + m^2 + n^2 = 2m^2 + 2mn
    # so we only need n, m such that 2m^2 + 2mn < 1000
    # We can solve for n: n < (1000 - 2m^2) / 2m
    # Since n must be > 0, we can bound n:
    # 0 < (1000 - 2m^2) / 2m => 2m^2 < 1000 => m < sqrt(1000/2)

    primes = tuple(sieve_of_eratosthenes(limit))
    bases = ((m, n) 
             for m in range(1, m_upper_bound(limit))
             for n in range(1, n_upper_bound(m, limit))
             if is_triple_base(m, n, primes))
        
    triples = [triple for m, n in bases for triple in generate_triples(m, n, limit)]
    counted = Counter(sum(triple) for triple in triples)
    perimiter = counted.most_common(1)[0][0]

    if verbose > 0:
        triples.sort()
        lines = ("{}^2 + {}^2 = {}^2".format(*t) for t in triples if sum(t) == perimiter)
        click.echo('\n'.join(lines))

    click.echo(perimiter)


def is_triple_base(m, n, primes):
    """Return if m and n are a valid pimitive triple base"""
    return (m % 2 == 0 or n % 2 == 0) \
        and m > n and n > 0 \
        and are_coprime(m, n, primes)


@memoize
def factor(n, primes):
    return set(factor_with_primes(n, primes))


@memoize
def are_coprime(a, b, primes):
    a_factors = factor(a, primes)
    b_factors = factor(b, primes)
    return len(a_factors & b_factors) == 0


def generate_triples(m, n, perimiter_limit):
    for k in count(1):
        triple = calculate_triple(m, n, k)
        if sum(triple) >= perimiter_limit:
            return
        yield triple


def calculate_triple(m, n, k=1):
    return (
        calculate_a(m, n, k), 
        calculate_b(m, n, k), 
        calculate_c(m, n, k))


def calculate_a(m, n, k=1):
    return k * (m**2 - n**2)


def calculate_b(m, n, k=1):
    return k * 2 * m * n


def calculate_c(m, n, k=1):
    return k * (m**2 + n**2)


def m_upper_bound(limit):
    return int(floor(sqrt(limit / 2)))


def n_upper_bound(m, limit):
    return int(ceil((limit - 2 * m ** 2) / (2 * m)))
