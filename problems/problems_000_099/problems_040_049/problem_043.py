

import click

from itertools import permutations
from tools.numbers import digit_count

@click.command('43')
@click.option('--verbose', '-v', count=True)
def problem_043(verbose):
    """Sub-string divisibility.

    The number, 1406357289, is a 0 to 9 pandigital number because it is made
    up of each of the digits 0 to 9 in some order, but it also has a rather
    interesting sub-string divisibility property.
    
    Let _d_1 be the 1st digit, _d_2 be the 2nd digit, and so on. In this way,
    we note the following:
    
      * _d_2_d_3_d_4=406 is divisible by 2
      * _d_3_d_4_d_5=063 is divisible by 3
      * _d_4_d_5_d_6=635 is divisible by 5
      * _d_5_d_6_d_7=357 is divisible by 7
      * _d_6_d_7_d_8=572 is divisible by 11
      * _d_7_d_8_d_9=728 is divisible by 13
      * _d_8_d_9_d_10=289 is divisible by 17
    
    Find the sum of all 0 to 9 pandigital numbers with this property.
    
    """

    digits = '0123456789'
    pandigital = (''.join(p) for p in permutations(digits))
    primes = [1, 2, 3, 5, 7, 11, 13, 17]
    with_property = (int(p) for p in pandigital if check_all(p, primes))
    all_numbers = list(with_property)
    click.echo(sum(all_numbers))
    

def check_all(number, divisors):
    for i, d in enumerate(divisors):
        if not check_substring_divisible(number, i, d):
            return False
    return True

def check_substring_divisible(number, index, divisor):
    value = int(number[index:index+3])
    return value % divisor == 0