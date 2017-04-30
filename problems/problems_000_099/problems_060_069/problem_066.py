

import click

from itertools import count
from tools.numbers import sqrt_continuted_fraction, is_perfect_square
from fractions import Fraction

@click.command('66')
@click.option('--limit', '-l', type=int, default=1000)
@click.option('--verbose', '-v', count=True)
def problem_066(limit,verbose):
    """Diophantine equation.

    Consider quadratic Diophantine equations of the form:
    
    _x_2 – D_y_2 = 1
    
    For example, when D=13, the minimal solution in _x_ is 6492 – 13×1802 = 1.
    
    It can be assumed that there are no solutions in positive integers when D
    is square.
    
    By finding minimal solutions in _x_ for D = {2, 3, 5, 6, 7}, we obtain the
    following:
    
    32 – 2×22 = 1  
    22 – 3×12 = 1  
    92 – 5×42 = 1  
    52 – 6×22 = 1  
    82 – 7×32 = 1
    
    Hence, by considering minimal solutions in _x_ for D ≤ 7, the largest _x_
    is obtained when D=5.
    
    Find the value of D ≤ 1000 in minimal solutions of _x_ for which the
    largest value of _x_ is obtained.
    
    """
    D_values = (D for D in range(1, limit + 1) if not is_perfect_square(D))
    solutions = [(D, find_fundemental_solution(D)) for D in D_values]
    maximal = max(solutions, key=lambda sol: sol[1][0])
    
    click.echo("{x}**2 - {d} * {y}**2 == 1".format(
        x=click.style(str(maximal[1][0]), bold=True),
        y=click.style(str(maximal[1][1]), bold=True),
        d=click.style(str(maximal[0]), fg='red', bold=True)))


def find_fundemental_solution(D):
    coefficients = sqrt_continuted_fraction(D)
    fractions = iterate_terms(coefficients)
    canditates = ((f.numerator, f.denominator) for f in fractions)
    solutions = ((x, y) for x, y in canditates if is_solution(D, x, y))
    return next(solutions, None)


def is_solution(D, x, y):
    return x**2 - D * y**2 == 1    


def iterate_terms(coefficients):
    for i in count():
        yield make_fraction_term(i, coefficients)


def make_fraction_term(term, coefficients):
    f = 0
    period = len(coefficients) - 1

    for n in range(term, 0, -1):
        f = Fraction(1, coefficients[((n - 1) % period) + 1] + f)

    return coefficients[0] + f
