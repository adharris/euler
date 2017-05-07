

import click

from tools.numbers import iter_digits
from math import factorial


@click.command('74')
@click.option('--limit', '-l', type=int, default=1000000)
@click.option('--verbose', '-v', count=True)
def problem_074(limit,verbose):
    """Digit factorial chains.

    The number 145 is well known for the property that the sum of the
    factorial of its digits is equal to 145:
    
    1! + 4! + 5! = 1 + 24 + 120 = 145
    
    Perhaps less well known is 169, in that it produces the longest chain of
    numbers that link back to 169; it turns out that there are only three such
    loops that exist:
    
    169 → 363601 → 1454 → 169  
    871 → 45361 → 871  
    872 → 45362 → 872
    
    It is not difficult to prove that EVERY starting number will eventually
    get stuck in a loop. For example,
    
    69 → 363600 → 1454 → 169 → 363601 (→ 1454)  
    78 → 45360 → 871 → 45361 (→ 871)  
    540 → 145 (→ 145)
    
    Starting with 69 produces a chain of five non-repeating terms, but the
    longest non-repeating chain with a starting number below one million is
    sixty terms.
    
    How many chains, with a starting number below one million, contain exactly
    sixty non-repeating terms?
    
    """

    known_lengths = {
        169: 3, 363601: 3, 1454: 3, 
        871: 2, 45361: 2,
        872: 2, 45362: 2,
    }
    factorials = {n: factorial(n) for n in range(10)}
    
    def transform(number):
        return sum(factorials[d] for d in iter_digits(number))

    def find_length(number):
        if number not in known_lengths:
            transformed = transform(number)
            length = 0 if transformed == number else find_length(transformed)
            known_lengths[number] = length + 1
        return known_lengths[number]

    with_sixty = (n for n in range(3, limit) if find_length(n) == 60)
    click.echo(sum(1 for _ in with_sixty))
