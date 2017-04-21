

import click

@click.command('1')
@click.option('--multiple', '-m', multiple=True, type=int, default=(3, 5),
              help='The base mulitiples to sum')
@click.option('--limit', '-l', default=1000, type=int,
              help='The limit for multuples')
def problem_001(multiple, limit):
    """Multiples of 3 and 5

    Sum the multiples of the natural numbers specified by the --muliple values
    that are less than --limit

    euler 1 -m 3 -m 5 -l 1000

    https://projecteuler.net/problem=1

    If we list all the natural numbers below 10 that are multiples of 3 or 5, 
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    numbers = set([])
    for value in multiple:
        mulitples = range(0, limit, value)
        numbers = numbers | set(mulitples)

    total = sum(numbers)
    click.echo(total)