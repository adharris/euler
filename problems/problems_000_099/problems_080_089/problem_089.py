

import click

from collections import OrderedDict
from itertools import zip_longest
from tools.memoization import Memoize
from pathlib import Path


@click.command('89')
@click.option('--verbose', '-v', count=True)
def problem_089(verbose):
    """Roman numerals.

    For a number written in Roman numerals to be considered valid there are
    basic rules which must be followed. Even though the rules allow some
    numbers to be expressed in more than one way there is always a "best" way
    of writing a particular number.
    
    For example, it would appear that there are at least six ways of writing
    the number sixteen:
    
    IIIIIIIIIIIIIIII  
    VIIIIIIIIIII  
    VVIIIIII  
    XIIIIII  
    VVVI  
    XVI
    
    However, according to the rules only XIIIIII and XVI are valid, and then
    last example is considered to be the most efficient, as it uses the least
    number of numerals.
    
    The 11K text file, [roman.txt](project/resources/p089_roman.txt) (right
    click and 'Save Link/Target As...'), contains one thousand numbers written
    in valid, but not necessarily minimal, Roman numerals; see [About... Roman
    Numerals](about=roman_numerals) for the definitive rules for this problem.
    
    Find the number of characters saved by writing each of these in their
    minimal form.
    
    Note: You can assume that all the Roman numerals in the file contain no
    more than four consecutive identical units.
    
    """

    difference = 0

    with Path('.', 'files', 'roman.txt').open('r') as f:
        for numeral in f.readlines():
            number = parse_numeral(numeral.strip())
            optimal = create_minimal(number)
            difference += len(numeral) - len(optimal) 
            print(optimal, numeral.strip(), number)

    click.echo(difference)


def parse_numeral(numeral):
    number = 0
    for char, next_char in zip_longest(numeral, numeral[1:]):
        if next_char and numerals[char] < numerals[next_char]:
            number -= numerals[char]
        else:
            number += numerals[char]
    return number


@Memoize()
def create_minimal(number):
    numeral = ""
    
    if number >= 1000:
        m_count = number // 1000
        numeral += m_count * 'M'
        number -= m_count * 1000

    if number >= 900:
        numeral += "CM"
        number -= 900

    if number >= 500:
        numeral += "D"
        number -= 500

    if number >= 400:
        numeral += 'CD'
        number -= 400

    if number >= 100:
        c_count = number // 100
        numeral += 'C' * c_count
        number -= 100 * c_count
        
    if number >= 90:
        numeral += 'XC'
        number -= 90

    if number >= 50:
        numeral += 'L'
        number -= 50

    if  number >= 40:
        numeral += 'XL'
        number -= 40

    if number >= 10:
        x_count = number // 10
        numeral += 'X' * x_count
        number -= 10 * x_count

    if number >= 9:
        numeral += 'IX'
        number -= 9

    if number >= 5:
        numeral += 'V'
        number -= 5

    if number >= 4:
        numeral += 'IV'
        number -= 4

    if number >= 1:
        numeral += number * 'I'
    
    return numeral


numerals = OrderedDict([
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000),   
])