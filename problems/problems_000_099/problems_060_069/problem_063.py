

import click
from tools.numbers import digit_count
from itertools import count

@click.command('63')
@click.option('--verbose', '-v', count=True)
def problem_063(verbose):
    """Powerful digit counts.

    The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
    9-digit number, 134217728=8^9, is a ninth power.
    
    How many _n_-digit positive integers exist which are also an _n_th power?
    """

    click.echo(len(list(generate_all_digit_powers())))
    

def generate_all_digit_powers():
    for exponent in count(1):
        powers = list(generate_digit_powers(exponent))
        if len(powers) == 0:
            return
        yield from powers

def generate_digit_powers(exponent):
    for base in count(1):
        v = base ** exponent
        digits = len(str(v))
        if digits == exponent:
            yield v
        if digits > exponent:
            return
