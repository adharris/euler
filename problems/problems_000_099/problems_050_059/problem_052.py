

import click

from itertools import count
from tools.numbers import digit_count



@click.command('52')
@click.option('--multiplier', '-m', type=int, default=6)
@click.option('--verbose', '-v', count=True)
def problem_052(multiplier, verbose):
    """Permuted multiples.

    It can be seen that the number, 125874, and its double, 251748, contain
    exactly the same digits, but in a different order.
    
    Find the smallest positive integer, _x_, such that 2_x_, 3_x_, 4_x_, 5_x_,
    and 6_x_, contain the same digits.
    
    """

    all_numbers = count(1)
    multipliers = range(2, multiplier + 1)
    
    # Filter out numbers which would have a different number of digits when
    # multiplied by the largest multiplier
    same_digits = (n for n in all_numbers if has_same_digits(n, n * multiplier))
    are_multiples = (n for n in same_digits if multiples_are_permutatons(n, multipliers))
    first = next(are_multiples)

    if verbose > 0:
        for m in multipliers:
            click.echo("{} * {} = {}".format(first, m, first * m))

    click.echo(first)



def has_same_digits(n, m):
    return digit_count(n) == digit_count(m)


def multiples_are_permutatons(number, multipliers):
    for m in multipliers:
        if not is_permutation(number, number * m):
            return False
    return True


def is_permutation(number_1, number_2):
    return sorted(str(number_1)) == sorted(str(number_2))
