

import click

from tools.numbers import iter_digits

@click.command('56')
@click.option('--limit', '-l', type=int, default=100)
@click.option('--verbose', '-v', count=True)
def problem_056(limit,verbose):
    """Powerful digit sum.

    A googol (10100) is a massive number: one followed by one-hundred zeros;
    100100 is almost unimaginably large: one followed by two-hundred zeros.
    Despite their size, the sum of the digits in each number is only 1.
    
    Considering natural numbers of the form, _ab_, where _a, b_ &lt; 100, what
    is the maximum digital sum?
    
    """

    numbers = (a**b for a in range(1, limit) for b in range(1, limit))
    sums = (sum(iter_digits(number)) for number in numbers)
    click.echo(max(sums))