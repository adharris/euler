
import click

from tools import factor_with_sieve

@click.command('3')
@click.argument('value', type=int, default=600851475143)
def problem_003(value):
    """Largest prime factor
    
    https://projecteuler.net/problem=3

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
    """
    click.echo(max(factor_with_sieve(value)))