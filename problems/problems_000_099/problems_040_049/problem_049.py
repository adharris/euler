

import click

from itertools import permutations, combinations
from tools.primes import sieve_of_eratosthenes

@click.command('49')
@click.option('--verbose', '-v', count=True)
def problem_049(verbose):
    """Prime permutations.

    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three terms are
    prime, and, (ii) each of the 4-digit numbers are permutations of one
    another.
    
    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit
    increasing sequence.
    
    What 12-digit number do you form by concatenating the three terms in this
    sequence?
    
    """

    primes = set(p for p in sieve_of_eratosthenes(9999) if p > 1000)
    four_digit_primes = sorted(primes)
    prime_sets = (prime_permutations(p, primes) for p in four_digit_primes)
    prime_sets = (s for s in prime_sets if len(s) >= 3)
    combos = (c for s in prime_sets for c in combinations(s, 3))
    with_splits = ((c, find_split(*c)) for c in combos)
    with_property = (v for v in with_splits if v[1] is not None)

    for result in with_property:
        click.echo('{0[0]} {0[1]} {0[2]} ({1})'.format(*result))


def find_split(a, b, c):
    return b - a if b - a == c - b else None


def prime_permutations(number, primes):
    perms = permutations(str(number))
    numbers = (int("".join(p)) for p in perms)
    found = {n for n in numbers if n in primes}
    primes.difference_update(found)
    return found