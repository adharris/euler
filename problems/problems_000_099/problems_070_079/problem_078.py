

import click

from itertools import count
from .problem_076 import ways_to_sum

from tools.memoization import Memoize

@click.command('78')
@click.option('--divisor', '-d', type=int, default=1000000)
@click.option('--verbose', '-v', count=True)
def problem_078(divisor,verbose):
    """Coin partitions.

    Let p(_n_) represent the number of different ways in which _n_ coins can
    be separated into piles. For example, five coins can be separated into
    piles in exactly seven different ways, so p(5)=7.
    
    OOOOO  
    ---  
    OOOO O  
    OOO OO  
    OOO O O  
    OO OO O  
    OO O O O  
    O O O O O  
      
    Find the least value of _n_ for which p(_n_) is divisible by one million.
    
    """

    # click.echo(partitions(20))
    # return

    # click.echo([partitions(i) for i in range(15)])
    # return

    for i in count(7):
        parts = partitions(i)
        if parts % divisor == 0:
            click.echo("{} has {} partitions".format(i, parts))
            return


@Memoize()
def partitions(number):

    if number < 0:
        return 0

    if number == 0:
        return 1

    total = 0

    for i in count(1):
        sign = -1 if (i - 1) % 4 > 1 else 1
        pent = generalized_pentagonal_number(i)
        if number - pent < 0:
            break
        total += sign * partitions(number - pent)
    
    return total


def generalized_pentagonal_number(n):
    if n % 2 == 0:
        return pentagonal_number(- n // 2)
    else :
        return pentagonal_number(n // 2 + 1)

def pentagonal_number(n):
    return (3 * n**2 - n) // 2
