

import click

from itertools import count
from tools.primes import PrimeCache, miller_rabin_test, deterministic_miller_rabin_test

@click.command('58')
@click.option('--limit', '-l', type=float, default=.1)
@click.option('--verbose', '-v', count=True)
def problem_058(limit,verbose):
    """Spiral primes.

    Starting with 1 and spiralling anticlockwise in the following way, a
    square spiral with side length 7 is formed.
    
    **37** 36 35 34 33 32 **31**  
    38 **17** 16 15 14 **13** 30  
    39 18  **5** 4  **3** 12 29  
    40 19 6 1 2 11 28  
    41 20  **7** 8 9 10 27  
    42 21 22 23 24 25 26  
    **43** 44 45 46 47 48 49
    
    It is interesting to note that the odd squares lie along the bottom right
    diagonal, but what is more interesting is that 8 out of the 13 numbers
    lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
    
    If one complete new layer is wrapped around the spiral above, a square
    spiral with side length 9 will be formed. If this process is continued,
    what is the side length of the square spiral for which the ratio of primes
    along both diagonals first falls below 10%?
    
    """

    corners = generate_corners()
    total, primes, sl = 1, 0, 1

    for i, corners in enumerate(corners):
        sl += 2
        for corner in corners:
            total += 1
            primes += 1 if deterministic_miller_rabin_test(corner) else 0
        if primes / total < limit:
            break
        
    click.echo(sl)


def generate_corners():
    for i in count(3, 2):
        yield tuple(i**2 - j * (i - 1) for j in range(4))
