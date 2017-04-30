

import click

from itertools import product, combinations
from tools.primes import deterministic_miller_rabin_test, sieve_of_eratosthenes


@click.command('60')
@click.option('--size', '-s', type=int, default=5)
@click.option('--verbose', '-v', count=True)
def problem_060(size,verbose):
    """Prime pair sets.

    The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
    primes and concatenating them in any order the result will always be
    prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
    sum of these four primes, 792, represents the lowest sum for a set of four
    primes with this property.
    
    Find the lowest sum for a set of five primes for which any two primes
    concatenate to produce another prime.
    
    """

    # Find pairs and add new items?

    primes = sieve_of_eratosthenes(9000)
    families = (f for f in make_families(primes, size))   
    click.echo(sum(next(families)))


def make_families(primes, n):
    for i, p1 in enumerate(primes):
        for j, p2 in enumerate(primes[:i]):
            if not is_concatable_pair(p1, p2):
                continue
            for fam in deeper(primes, (p1, p2), j, n - 2):
                yield fam
            
def deeper(primes, family, end, n):
    if n == 0:
        yield family
        return

    for i, p in enumerate(primes[:end]):
        if not can_add_to_family(p, family):
            continue
            
        for fam in deeper(primes, family + (p, ), i, n - 1):
            yield fam


def can_add_to_family(prime, family):
    for other in family:
        if not is_concatable_pair(prime, other):
            return False
    return True


def is_family_concatable(primes):
    pairs = ((a, b) for a in primes for b in primes if a != b)
    for a, b in pairs:
        if not concat_is_prime(a, b):
            return False
    return True


def is_concatable_pair(a, b):
    return concat_is_prime(a, b) and concat_is_prime(b, a)


def concat_is_prime(a, b):
    return deterministic_miller_rabin_test(int(str(a) + str(b)))