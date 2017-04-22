

import click

from tools.numbers import digit

@click.command('17')
@click.option('--limit', '-l', type=int, default=1000)
@click.option('--number', '-n', type=int, default=None)
def problem_017(limit, number):
    """Number letter counts

    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    
    If all the numbers from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?
    
    **NOTE:** Do not count spaces or hyphens. For example, 342 
        (three hundred and forty-two) contains 23 letters and 115 
        (one hundred and fifteen) contains 20 letters. The use of "and" 
        when writing out numbers is in compliance with British usage.
    """

    if number is not None:
        click.echo(number_to_string(number))
        click.echo(len(number_to_string(number)))
    else:
        strings = (number_to_string(n) for n in range(1, limit + 1))
        lengths = (len(s) for s in strings)
        click.echo(sum(lengths))
        

def number_to_string(number):
    parts = []
    thousands = digit(number, 3)
    if thousands > 0:
        parts.append('{}thousand'.format(number_names[thousands]))

    hundreds = digit(number, 2)
    if hundreds > 0:
        parts.append('{}hundred'.format(number_names[hundreds]))
        
    tens = digit(number, 1)
    ones = digit(number, 0)
    
    if len(parts) > 0 and tens + ones > 0:
        parts.append('and')
        
    if tens == 0 and ones == 0:
        pass
    elif tens == 0:
        parts.append(number_names[ones])
    elif tens == 1:
        parts.append(teens[ones])
    elif ones == 0:
        parts.append(ten_names[tens])
    elif tens != 0 and ones != 0:
        parts.append("{}{}".format(ten_names[tens], number_names[ones]))

    return "".join(parts)

number_names = [
    None,
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

teens = [
    'ten',
    'eleven',
    'twelve',
    'thriteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]

ten_names = [
    None,
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]

hundred = 'hundred'
thousand = 'thousand'

