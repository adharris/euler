

import click
from tools import sieve_of_eratosthenes

@click.command('10')
@click.option('--limit', '-l', type=int, default=2000000)
def problem_010(limit):
    """Summation of primes

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    
    Find the sum of all the primes below two million.
    
    """

    primes = sieve_of_eratosthenes(limit)
    click.echo(sum(primes))