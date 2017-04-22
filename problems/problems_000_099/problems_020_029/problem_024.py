
import click
from itertools import permutations, islice
from tools.numbers import digits_to_number

@click.command('24')
@click.option('--number', '-n', type=int, default=1000000)
def problem_024(number):
    """Lexicographic permutations

    A permutation is an ordered arrangement of objects. For example, 3124 is
    one possible permutation of the digits 1, 2, 3 and 4. If all of the
    permutations are listed numerically or alphabetically, we call it
    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
    
    012 021 102 120 201 210
    
    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
    4, 5, 6, 7, 8 and 9?
    
    """
    digits = range(0, 10)
    perms = permutations(digits)
    sliced = islice(perms, number -1, number)
    digits = next(sliced)
    number = digits_to_number(reversed(digits))
    click.echo(number)