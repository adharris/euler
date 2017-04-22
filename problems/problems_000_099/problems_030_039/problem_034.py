

import click
from math import factorial
from tools.numbers import iter_digits

@click.command('34')
@click.option('--verbose', '-v', count=True)
def problem_034(verbose):
    """Digit factorials.

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
    
    Find the sum of all numbers which are equal to the sum of the factorial of
    their digits.
    
    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    
    """

    # Cache factorials
    factorials = {n: factorial(n) for n in range(10)}

    # The largest value for a number with n digits is n * 9!.  So the upper 
    # bound is the first number 10**(n + 1) - 1 which is greater than n * 9!
    # we can quickly iterate to find it.

    upper_bound = next(
        n * factorials[9] for n in range(1, 100)
        if n * factorials[9] < 10**(n + 1) -1)

    candidates = range(3, upper_bound)
    bar = click.progressbar(candidates)
    with bar:
        curious_numbers = [n for n in bar if is_curious(factorials, n)]
                       
    if verbose >= 1:
        for n in curious_numbers:
            print_curious_number(n)
    
    click.echo(sum(curious_numbers))
    

def print_curious_number(n):
    parts = ("{}!".format(d) for d in iter_digits(n))
    joined = " + ".join(parts)
    click.echo("{} = {}".format(joined, n))

def is_curious(cache, number):
    return number == sum_factorials(cache, number)


def sum_factorials(cache, number):
    return sum(cache[d] for d in iter_digits(number))