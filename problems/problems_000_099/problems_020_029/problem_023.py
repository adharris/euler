

import click

from tools.primes import PrimeCache


@click.command('23')
def problem_023():
    """Non-abundant sums

    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors
    of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number.
    
    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.
    
    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
    smallest number that can be written as the sum of two abundant numbers is
    24. By mathematical analysis, it can be shown that all integers greater
    than 28123 can be written as the sum of two abundant numbers. However,
    this upper limit cannot be reduced any further by analysis even though it
    is known that the greatest number that cannot be expressed as the sum of
    two abundant numbers is less than this limit.
    
    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.
    
    """

    known_lower_bound = 12
    known_upper_bound = 28123
    primes = PrimeCache(known_upper_bound)
    numbers = range(known_lower_bound, known_upper_bound)
    bar = click.progressbar(numbers, label='Generating Abundent numbers')
    with bar:
        abundent = [n for n in bar if is_abundent(primes, n)]
        
    largest = abundent[-1] + abundent[-2]
    candidates = set(range(1, known_upper_bound))
    print(abundent[-1])
    with click.progressbar(abundent, label='Eliminating sums') as bar:
        for i, a in enumerate(bar):
            for b in abundent[i:]:
                candidates.discard(a + b)

    click.echo(sum(candidates))


def is_abundent(primes, number):
    divisors = primes.proper_divisors(number)
    total = sum(divisors)
    return total > number