

import click

from collections import namedtuple

from  math import sqrt

@click.command('85')
@click.option('--target', '-t', type=int, default=2000000)
@click.option('--verbose', '-v', count=True)
def problem_085(target, verbose):
    """Counting rectangles.

    By counting carefully it can be seen that a rectangular grid measuring 3
    by 2 contains eighteen rectangles:
    
    ![](project/images/p085.gif)
    
    Although there exists no rectangular grid that contains exactly two
    million rectangles, find the area of the grid with the nearest solution.
    
    """

    # The number of rectangles is the product of the triangle numbers of the
    # sides:
    # 
    # R(w, l) = (w(w + 1)/2)(l(l+1)/2)

    guesses = enumerate_guesses(target)
    w, l = min(guesses, key=lambda g: abs(rectangle_count(*g) - target))

    click.echo("R({}x{}) = {}".format(w, l, rectangle_count(w, l)))
    click.echo("{}x{} = {}".format(w, l, w * l))


def enumerate_guesses(target):
    width = 0

    while True:
        width += 1
        length = find_best_length(width, target)
        
        if length < width:
            break
        
        yield (width, int(length))
        yield (width, int(length) + 1)


def rectangle_count(width, length):
    return ((width**2 + width) // 2) * ((length**2 + length) // 2)


def find_best_length(width, rectangle_count):
    a = (width**2 + width) / 4
    b = a
    c = -rectangle_count
    return (-b + sqrt(b**2 - 4 * a *c)) / (2 * a)
