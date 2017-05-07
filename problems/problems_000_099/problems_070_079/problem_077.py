

import click

from tools.primes import sieve_of_eratosthenes
from tools.memoization import Memoize
from itertools import takewhile


@click.command('77')
@click.option('--limit', '-l', type=int, default=5000)
@click.option('--verbose', '-v', count=True)
def problem_077(limit,verbose):
    """Prime summations.

    It is possible to write ten as the sum of primes in exactly five different
    ways:
    
    7 + 3  
    5 + 5  
    5 + 3 + 2  
    3 + 3 + 2 + 2  
    2 + 2 + 2 + 2 + 2
    
    What is the first value which can be written as the sum of primes in over
    five thousand different ways?
    
    """

    prime_limit = 100
    all_primes = sieve_of_eratosthenes(prime_limit)

    for i in range(4, prime_limit):
    
        primes = tuple(takewhile(lambda p: p < i, all_primes))
        ways = ways_to_sum_with_primes(i, primes)
        
        if ways > limit:
            click.echo("{}: {} ways".format(i, ways))
            return


@Memoize(arg_count=2)
def ways_to_sum_with_primes(number, primes):

    if number == 0:
        return 0
        
    if len(primes) == 0:
        return None

    total = 0

    for i, prime in enumerate(reversed(primes)):
    
        if prime > number:
            continue

        for count in range(number // prime, 0, -1):
            remaining = number - prime * count

            if remaining == 0:
                total += 1
                continue

            ways = ways_to_sum_with_primes(remaining, primes[:-(i + 1)])
            if ways is not None:
                total += ways
    
    return total


"""

5
3 + 2

12


11 + 1
7 + 5
7 + 3 + 2
5 + 5 + 2
5 + 3 + 2 + 2
3 + 3 + 2 + 2 + 2
2 + 2 + 2 + 2 + 2 + 2
7

15
7 + 5 + 3
7 + 3 + 3 + 2
7 + 2 + 2 + 2 + 2 
5 + 5 + 5
5 + 5 + 3 + 2
5 + 3 + 3 + 2 + 2
5 + 2 + 2 + 2 + 2 + 2
3 + 2 + 2 + 2 + 2 + 2 + 2

25

23 + 2
19 + 3 + 3
19 + 2 + 2 + 2
17 + 5 + 3
17 + 3 + 3 + 2
17 + 2 + 2 + 2 + 2 + 2 + 2
13 + 11 + 1
13 + 7 + 5
13 + 5 + 5 + 2 
13 + 5 + 3 + 2 + 2
13 + 3 + 3 + 2 + 2 + 2 
13 + 2 + 2 + 2 + 2 + 2 + 2
11 + 11 + 3
11 + 7 + 7
11 + 7 + 3 + 2 + 2
11 + 5 + 5 + 2 + 2
1


""" 