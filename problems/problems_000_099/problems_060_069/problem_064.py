

import click
from collections import namedtuple
from math import sqrt


@click.command('64')
@click.option('--limit', '-l', type=int, default=10000)
@click.option('--verbose', '-v', count=True)
def problem_064(limit, verbose):
    """Odd period square roots.

    All square roots are periodic when written as continued fractions and can
    be written in the form:
   
    It can be seen that the sequence is repeating. For conciseness, we use the
    notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
    indefinitely.
    
    The first ten continued fraction representations of (irrational) square
    roots are:
    
    √2=[1;(2)], period=1  
    √3=[1;(1,2)], period=2  
    √5=[2;(4)], period=1  
    √6=[2;(2,4)], period=2  
    √7=[2;(1,1,1,4)], period=4  
    √8=[2;(1,4)], period=2  
    √10=[3;(6)], period=1  
    √11=[3;(3,6)], period=2  
    √12= [3;(2,6)], period=2  
    √13=[3;(1,1,1,1,6)], period=5
    
    Exactly four continued fractions, for N ≤ 13, have an odd period.
    
    How many continued fractions for N ≤ 10000 have an odd period?
    
    """

    numbers = range(2, limit + 1)
    fractions = (create_continued_fraction(sqrt(n)) for n in numbers)
    irrational = (f for f in fractions if len(f.coefficents) > 0)
    odd = (f for f in fractions if len(f.coefficents) % 2 == 1)

    for f in odd:
        click.echo(len(list(odd)))


ContinuedFraction = namedtuple('ContinuedFraction', 'integer coefficents fractional')



def create_continued_fraction(number):
    integer_part = int(number)
    fractional_part = number - integer_part
    cf = ContinuedFraction(integer_part, tuple(), fractional_part)
    if cf.fractional == 0:
        return cf
    cf = continue_fraction(cf)
    while cf.coefficents[-1] != cf.integer * 2 and cf.fractional != 0:
        cf = continue_fraction(cf)
    return cf


def continue_fraction(continued_fraction):
    reciprocal = 1 / continued_fraction.fractional
    integer_part = int(reciprocal)
    fractional_part = reciprocal - integer_part
    return ContinuedFraction(
        continued_fraction.integer,
        continued_fraction.coefficents + (integer_part, ),
        fractional_part)


def format_continuted_fraction(f):
    period = "({})".format(", ".join(str(n) for n in f.coefficents))
    return "⟨{}; {}⟩".format(f.integer, period)