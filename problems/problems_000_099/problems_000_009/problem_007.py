

import click
from tools import unbounded_sieve_of_eratosthenes

@click.command('7')
@click.argument('ordinal', type=int, default=10001)
def problem_007(ordinal):
    """10001st prime

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
    that the 6th prime is 13.
    
    What is the 10001st prime number?
    
    """

    primes = unbounded_sieve_of_eratosthenes()

    for _ in range(ordinal):
        prime = next(primes)

    click.echo(prime)
