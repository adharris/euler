

import click

from itertools import permutations, chain
from tools.numbers import digits_to_number
from math import factorial

@click.command('32')
@click.option('--digits', '-d', type=int, default=9)
@click.option('--verbose', '-v', count=True)
def problem_032(digits, verbose):
    """Pandigital products

    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
    1 through 5 pandigital.
    
    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.
    
    Find the sum of all products whose multiplicand/multiplier/product
    identity can be written as a 1 through 9 pandigital.
    
    HINT: Some products can be obtained in more than one way so be sure to
    only include it once in your sum.
    
    """

    chars = (str(d) for d in range(1, digits + 1))
    perms = permutations(chars)
    perms = ("".join(p) for p in perms)
    
    with click.progressbar(perms, length=factorial(digits)) as bar:
        splits = (s for perm in bar for s in split(perm))
        matches = {s for s in splits if is_product(s)}

    if verbose > 0:
        for m in matches:
            click.echo("{} × {} = {}".format(*m))
    click.echo(sum({m[2] for m in matches}))
            

def split(digits):
    for i in range(1, 5):
        for j in range(i + 1, i + 4):
            yield (int(digits[:i]), int(digits[i:j]), int(digits[j:]))


def is_product(splits):
    return splits[0] * splits[1] == splits[2]