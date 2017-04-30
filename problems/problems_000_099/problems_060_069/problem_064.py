

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
    bar = click.progressbar(numbers)
    with bar:
        fractions = (find_continuted_fraction(n) for n in bar)
        irrational = (f for f in fractions if len(f.coefficents) > 0)
        odd = [f for f in fractions if len(f.coefficents) % 2 == 1]
        
    if verbose:
        lines = ["√{} = {}".format(f.base, format_continuted_fraction(f)) for f in odd]
        click.echo_via_pager("\n".join(lines))       
    
    click.echo(len(list(odd)))


ContinuedFraction = namedtuple('ContinuedFraction', 'integer coefficents base')


def find_continuted_fraction(number):
    """https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion"""

    if int(sqrt(number)) == sqrt(number):
        return ContinuedFraction(int(sqrt(number)), (), number)

    m = 0
    d = 1
    a = [int(sqrt(number)) ]

    while a[-1] != a[0] * 2:
        m = d * a[-1] -  m
        d = (number - m**2) // d
        next_a = int((a[0] + m) / d)
        a.append(next_a)

    return ContinuedFraction(a[0], a[1:], number)


def format_continuted_fraction(f):
    period = "({})".format(", ".join(str(n) for n in f.coefficents))
    return "⟨{}; {}⟩".format(f.integer, period)