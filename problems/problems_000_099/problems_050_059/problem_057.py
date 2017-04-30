

import click
from fractions import Fraction
from tools.numbers import digit_count

@click.command('57')
@click.option('--limit', '-l', type=int, default=1000)
@click.option('--verbose', '-v', count=True)
def problem_057(limit, verbose):
    """Square root convergents.

    It is possible to show that the square root of two can be expressed as an
    infinite continued fraction.
    
    √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
    
    By expanding this for the first four iterations, we get:
    
    1 + 1/2 = 3/2 = 1.5  
    1 + 1/(2 + 1/2) = 7/5 = 1.4  
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...  
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...  
    
    The next three expansions are 99/70, 239/169, and 577/408, but the eighth
    expansion, 1393/985, is the first example where the number of digits in
    the numerator exceeds the number of digits in the denominator.
    
    In the first one-thousand expansions, how many fractions contain a
    numerator with more digits than denominator?
    
    """
    terms = (term(n) for n in range(limit))
    terms = [t for t in terms if digit_count(t.numerator) > digit_count(t.denominator)]
    click.echo(len(terms))

def term(n):
    if n == 1:
        return 1
    fract = Fraction(1, 2)
    for i in range(n-2):
        fract = Fraction(1, 2 + fract)
    return 1 + fract