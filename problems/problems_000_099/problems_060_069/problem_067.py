

import click

from pathlib import Path
from operator import add

@click.command('67')
def problem_067():
    """Maximum path sum II

    By starting at the top of the triangle below and moving to adjacent
    numbers on the row below, the maximum total from top to bottom is 23.
    
    **3**  
    **7** 4  
    2 **4** 6  
    8 5 **9** 3
    
    That is, 3 + 7 + 4 + 9 = 23.
    
    Find the maximum total from top to bottom in
    [triangle.txt](project/resources/p067_triangle.txt) (right click and 'Save
    Link/Target As...'), a 15K text file containing a triangle with one-
    hundred rows.
    
    **NOTE:** This is a much more difficult version of [Problem 18](problem=18). It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
    
    """

    triangle = load_triangle()
    while len(triangle) > 1:
        triangle = reduce_triangle(triangle, max, add)
    click.echo(triangle[0][0])


def reduce_triangle(triangle, pick, combine):
    ultimate = triangle[-1]
    penultimate = triangle[-2]
    new_row = tuple(
        combine(value, pick(ultimate[i], ultimate[i + 1]))
        for i, value in enumerate(penultimate))
    return triangle[:-2] + (new_row, )


def load_triangle():
    with Path('.', 'files', 'triangle.txt').open('r') as f:
        return tuple(
            tuple(int(i) for i in line.split(' '))
            for line in f.readlines()
        )