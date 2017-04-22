

import click

from tools.numbers import digit_count
from tools.primes import sieve_of_eratosthenes


@click.command('41')
@click.option('--verbose', '-v', count=True)
def problem_041(verbose):
    """Pandigital prime.

    We shall say that an _n_-digit number is pandigital if it makes use of all
    the digits 1 to _n_ exactly once. For example, 2143 is a 4-digit
    pandigital and is also prime.
    
    What is the largest _n_-digit pandigital prime that exists?
    
    """
    primes = list(sieve_of_eratosthenes(10**8))
    primes = reversed(primes)
    pandigit = (p for p in primes if is_pandigital(p))
    click.echo(next(pandigit), None)


def is_pandigital(number):
    digits = '123456789'[:digit_count(number)]
    return ''.join(sorted(str(number))) == digits