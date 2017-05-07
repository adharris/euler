

import click

from tools.memoization import Memoize

@click.command('76')
@click.option('--number', '-n', type=int, default=100)
@click.option('--verbose', '-v', count=True)
def problem_076(number, verbose):
    """Counting summations.

    It is possible to write five as a sum in exactly six different ways:
    
    4 + 1  
    3 + 2  
    3 + 1 + 1  
    2 + 2 + 1  
    2 + 1 + 1 + 1  
    1 + 1 + 1 + 1 + 1
    
    How many different ways can one hundred be written as a sum of at least
    two positive integers?
    
    """

    # We can write N using the following sums:
    # 
    #  (N - 1) + 1
    #  (N - 2) + 2
    #  (N - (N - 1)) + N - 1 = 1 + (N - 1)
    # 
    #  Therefore, ways to sum for N is sum(ways to sum n - i) for i < N

    click.echo(ways_to_sum(number, number))


@Memoize()
def ways_to_sum(value, limit=None):

    limit = value if limit is None else limit

    if limit == 2:
        return 1
    
    total = 1

    for first_number in range(limit - 1, 1, -1):
        for multiples in range(value // first_number, 0, -1):
            remaining = value - first_number * multiples
            total += ways_to_sum(remaining, first_number)
            
    return total

"""
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1

c(4) = 4

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
c(5) = 6

5 + 1
4 + 2
4 + 1 +1
3 + 3
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 2
2 + 2 + 1 + 1
2 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1

c(6) = 10

6 + 1
5 + 2
5 + 1 + 1
4 + 3
4 + 2 + 1
4 + 1 + 1 + 1
3 + 3 + 1
3 + 2 + 2
3 + 2 + 1 + 1
3 + 1 + 1 + 1 + 1
2 + 2 + 2 + 1
2 + 2 + 1 + 1 + 1
2 + 1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1 + 1 

c(7) = 14

"""