
import click
from collections import Counter
from tools import sieve_of_eratosthenes, factor_with_primes


@click.command('5')
@click.option('--limit', '-l', type=int, default=20)
@click.option('--verbose', '-v', count=True)
def problem_005(limit, verbose):
    """Smallest multiple

    Smallest multiple is the product of the unique primes in all the numbers.
    Calculate the primes up to limit, factor each of the numbers up to limit,
    keeping track of the max time each prime is used. Then mulitple.

    Runs quickly for limit up to 10e5.

    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    """


    primes = sieve_of_eratosthenes(limit + 1)
    factors = Counter()

    for value in range(2, limit + 1):
        counts = Counter(factor_with_primes(value, primes))
        for prime, count in counts.items():
            factors[prime] = max(factors[prime], count)
    
    product = 1
    for prime, count in factors.items():
        product = product * prime ** count

    if verbose > 0:
        click.echo(prime_expression(factors))
    
    if verbose > 1:
        for value in range(1, limit + 1):
            assert product % value == 0
            click.echo('{} / {} = {}'.format(product, value, product / value))

    click.echo(product)


def prime_expression(factors):
    items = sorted(factors.items(), reverse=True)
    return " * ".join(format_prime(p, c) for p, c in items)


def format_prime(prime, count):
    if count > 1:
        return "{}**{}".format(prime, count)
    else:
        return str(prime)