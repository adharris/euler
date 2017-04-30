

import click
from tools.memoization import memoize
from math import factorial

@click.command('53')
@click.option('--limit', '-l', type=int, default=100)
@click.option('--threshold', '-t', type=int, default=1000000)
@click.option('--verbose', '-v', count=True)
def problem_053(limit, threshold, verbose):
    """Combinatoric selections.

    There are exactly ten ways of selecting three from five, 12345:
    
    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
    
    In combinatorics, we use the notation, 5C3 = 10.
    
    In general,
    
    nCr =  |
    
    n!  
    r!(n−r)!
    
    | ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.  
    ---|---|---  
      
    It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
    
    How many, not necessarily distinct, values of nCr, for 1 ≤ n ≤ 100, are
    greater than one-million?
    
    """

    numbers = range(1, limit + 1)
    pairs = ((n, r) for n in numbers for r in range(1, n + 1))
    combos = ((n, r, combinations(n, r)) for n, r in pairs)
    over_threshold = (combo for combo in combos if combo[2] > threshold)
    click.echo(len(list(over_threshold)))


factorial = memoize(factorial)

@memoize
def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
