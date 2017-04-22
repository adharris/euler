
import click

from itertools import count
from tools.series import yield_terms
from functools import reduce
from operator import mul


@click.command('40')
@click.option('--limit', '-l', type=int, default=7)
@click.option('--verbose', '-v', count=True)
def problem_040(limit,verbose):
    """Champernowne's constant.

    An irrational decimal fraction is created by concatenating the positive
    integers:
    
    0.123456789101112131415161718192021...
    
    It can be seen that the 12th digit of the fractional part is 1.
    
    If _d__n_ represents the _n_th digit of the fractional part, find the
    value of the following expression.
    
    _d_1 × _d_10 × _d_100 × _d_1000 × _d_10000 × _d_100000 × _d_1000000
    
    """

    indexes = (10**i for i in range(limit))
    items = list(yield_terms(generate_digits(), indexes))
    product = reduce(mul, items, 1)
    
    if verbose > 0:
        exp = ' × '.join(str(i) for i in items)
        click.echo("{} = {}".format(exp, product))

    click.echo(product)


def generate_digits():
    for number in count():
        for digit in str(number):
            yield int(digit)