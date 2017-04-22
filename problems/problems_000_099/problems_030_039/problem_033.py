

import click
from fractions import Fraction
from operator import mul
from functools import reduce

@click.command('33')
@click.option('--verbose', '-v', count=True)
def problem_033(verbose):
    """Digit cancelling fractions

    The fraction 49/98 is a curious fraction, as an inexperienced
    mathematician in attempting to simplify it may incorrectly believe that
    49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
    
    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
    
    There are exactly four non-trivial examples of this type of fraction, less
    than one in value, and containing two digits in the numerator and
    denominator.
    
    If the product of these four fractions is given in its lowest common
    terms, find the value of the denominator.
    
    """

    values = range(10, 99)
    pairs = ((a, b) for a in values for b in values)
    fractions = (
        ((a, b), (c, d))
        for a, b in pairs
        for c, d in digit_cancel(a, b))
    equal = ((Fraction(*a), a, b) for a, b in fractions 
             if Fraction(*a) == Fraction(*b))
             
    equal = list(sorted(equal))
    if verbose >=0:
        for item in equal:
            click.echo("{} = {}/{} = {}/{} ".format(
                item[0],
                item[1][0], item[1][1],
                item[2][0], item[2][1]))
    
    click.echo(reduce(mul, (i[0] for i in equal), 1))

def digit_cancel(a, b):
    if a >= b:
        return

    for digit in str(a):
        if digit == '0':
            continue
        try:
            new_a = int(str(a).replace(digit, ''))
            new_b = int(str(b).replace(digit, ''))
        except ValueError:
            continue
        
        if new_a == a or new_b == b or new_b == 0:
            continue

        yield (new_a, new_b)
            