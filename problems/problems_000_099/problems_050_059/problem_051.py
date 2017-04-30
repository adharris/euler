
from itertools import combinations
from tools.primes import sieve_of_eratosthenes
from tools.numbers import digit_count, set_digit

import click

@click.command('51')
@click.option('--size', '-s', type=int, default=8)
@click.option('--verbose', '-v', count=True)
def problem_051(size,verbose):
    """Prime digit replacements.

    By replacing the 1st digit of the 2-digit number *3, it turns out that six
    of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
    
    By replacing the 3rd and 4th digits of 56**3 with the same digit, this
    5-digit number is the first example having seven primes among the ten
    generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
    56773, and 56993. Consequently 56003, being the first member of this
    family, is the smallest prime with this property.
    
    Find the smallest prime which, by replacing part of the number (not
    necessarily adjacent digits) with the same digit, is part of an eight
    prime value family.
    
    """

    primes = sieve_of_eratosthenes(1000000)
    prime_set = set(primes)
    with click.progressbar(primes) as bar:
        families = (list(fam) for p in bar for fam in create_families(p))
        families = ([p for p in family if p in prime_set] for family in families)
        families = (f for f in families if len(f) >= size)
        first = sorted(next(families))
        bar.finish()
        
    click.echo(first)


def create_families(number):
    for template in create_templates(number):
        yield expand_all(template)


def create_templates(number):
    for i in range(1, digit_count(number)):
        for combo in combinations(range(digit_count(number)), i):
            yield (number, combo)


def expand_all(template):
    lower = 1 if digit_count(template[0]) - 1 in template[1] else 0
    for i in range(lower, 10):
        yield expand_template(template, i)


def expand_template(template, value):
    number = template[0]
    for digit in template[1]:
        number = set_digit(number, digit, value)
    return number