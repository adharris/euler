

import click

from tools.primes import PrimeCache
from tools.numbers import digit_count


@click.command('35')
@click.option('--limit', '-l', type=int, default=1000000)
@click.option('--verbose', '-v', count=True)
def problem_035(limit,verbose):
    """Circular primes.

    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.
    
    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.
    
    How many circular primes are there below one million?
    
    """

    cache = PrimeCache(limit + 1)
    cache.ensure_factors_for(limit)
    primes = set(cache.primes)
    
    with click.progressbar(primes) as bar:
        circular = [p for p in bar if is_circular_prime(primes, p)]
        
    if verbose > 0:
        circular.sort()
        lines = ("{}: {}".format(p, ', '.join(str(n) for n in rotate_number(p))) for p in circular)
        result = '\n'.join(lines)
        if len(circular) > 100:
            click.echo_via_pager(result)
        else:
            click.echo(result)
        
    click.echo(len(circular))


def is_circular_prime(all_primes, prime):
    for rotation in rotate_number(prime):
        if rotation not in all_primes:
            return False
    return True


def rotate_number(n):
    digits = digit_count(n)
    for i in range(digits):
        d = n % 10
        n = n // 10 + d * 10**(digits - 1)
        yield n