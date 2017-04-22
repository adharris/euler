

import click
from tools.primes import sieve_of_eratosthenes

@click.command('26')
@click.option('--limit', '-l', type=int, default=1000)
def problem_026(limit):
    """Reciprocal cycles

    A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:
    
    > 1/2| = | 0.5  
    > ---|---|---  
    > 1/3| = | 0.(3)  
    > 1/4| = | 0.25  
    > 1/5| = | 0.2  
    > 1/6| = | 0.1(6)  
    > 1/7| = | 0.(142857)  
    > 1/8| = | 0.125  
    > 1/9| = | 0.(1)  
    > 1/10| = | 0.1  
      
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
    be seen that 1/7 has a 6-digit recurring cycle.
    
    Find the value of _d_ &lt; 1000 for which 1/_d_ contains the longest
    recurring cycle in its decimal fraction part.
    
    """
    primes = sieve_of_eratosthenes(limit)
    parts = ((repeating_parts(p), p) for p in primes)
    largest = max(parts)
    click.echo(largest[1])


def repeating_parts(denominator):
    if denominator % 2 == 0: return 0
    if denominator % 5 == 0: return 0
    k = 1
    while True:
        if 10**k % denominator == 1:
            return k
        k += 1