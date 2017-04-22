

import click
from math import factorial
from tools.numbers import iter_digits

@click.command('20')
@click.option('--number', '-n', type=int, default=100)
def problem_020(number):
    """Factorial digit sum

    _n_! means _n_ × (_n_ − 1) × ... × 3 × 2 × 1
    
    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,  
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 =
    27.
    
    Find the sum of the digits in the number 100!
    """

    click.echo(sum(iter_digits(factorial(number))))