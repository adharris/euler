

import click

from tools.numbers import digit, digit_count

@click.command('16')
@click.option('--exponent', '-e', type=int, default=1000)
def problem_016(exponent):
    """Power digit sum

    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    
    What is the sum of the digits of the number 2^1000?
    """

    value = 2**exponent
    total = sum(digit(value, i) for i in range(digit_count(value)))
    click.echo(total)