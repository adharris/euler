
import click
from math import floor, ceil, log
from itertools import product

@click.command('4')
@click.option('--digits', '-d', type=int, default=3,
               help='The number of digits each number should have')
@click.option('--method', '-m', 
              type=click.Choice(['pair', 'product']), 
              default='product')
def problem_004(digits, method):
    """Largest palindrome product
    
    Finds the largest palindromic number which is a product of 2 N-digit 
    numbers.

    Provide 2 methods:

    'pairs' enumerates all n-digit pairs and attempts checks if their product is
    a palindromic number. It works for n=3.

    'product' works by generating palindromic numbers first and then attempting
    to find 2 n-digit factors.  It works in reasonable amount of time up to n=6.

    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 * 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """

    if method == 'pair':
        largest = pair_method(digits)
    else:
        largest = product_method(digits)

    click.echo("{} = {} * {}".format(*largest))
    

def pair_method(digits):
    largest = (0, 0, 0)

    with click.progressbar(digit_pairs(digits), length=pair_count(digits)) as bar:
        for number_1, number_2 in bar:
            product = number_1 * number_2
            if is_palindromic_number(product) and product > largest[0]:
                largest = (product, number_1, number_2)
    
    return largest

def pair_count(digits):
    number_count = 9 * 10 ** (digits - 1)
    pairs = number_count ** 2
    unique_pairs = (pairs - number_count) / 2
    return unique_pairs


def digit_range(digits):
    lower_bound = 10 ** (digits - 1)
    upper_bound = 10 ** (digits)
    for n in range(lower_bound, upper_bound):
        yield n

def digit_pairs(digits):
    lower_bound = 10 ** (digits - 1)
    upper_bound = 10 ** (digits) - 1
    for n1 in range(lower_bound, upper_bound):
        for n2 in range(lower_bound, n1 + 1):
            yield (n1, n2)


def is_palindromic_number(number):
    as_string = str(number)
    length = len(as_string)
    for index in range(0, length / 2):
        if as_string[index] != as_string[length - 1 - index]:
            return False
    return True


def product_method(digits):
    bounds = get_product_bounds(digits)
    for number in generate_palindromic_numbers_between(*bounds):
        factors = find_digit_factors(number, digits)
        if factors is not None:
            return (number, ) + factors


def find_digit_factors(number, digits):
    for n in digit_range(digits):
        if number % n == 0 and digit_count(number / n) == digits:
            return (n, number / n)
    return None


def digit_count(number):
    return len(str(number))


def get_product_bounds(digits):
    lower = 10 ** (digits - 1)
    upper = 10 ** (digits) - 1
    return lower ** 2, upper ** 2

    
def generate_palindromic_numbers_between(min, max):
    most_digits = len(str(max))
    least_digits = len(str(min))
    for digits in range(most_digits, least_digits -1, -1):
        for palindrome in generate_palindromic_numbers(digits):
            yield palindrome


def generate_palindromic_numbers(digits):
    to_generate = int(ceil(digits / 2.0))
    to_mirror = int(floor(digits / 2.0))
    minimum = 10 ** (digits - 1)
    for numbers in product(range(9, -1, -1), repeat=to_generate):
        palindrome = 0
        numbers = numbers + numbers[0:to_mirror][::-1]
        palindrome = sum(n * 10 ** i for i, n in enumerate(numbers))
                
        if palindrome > minimum:
            yield palindrome