

import click
from math import factorial

@click.command('15')
@click.option('--lattice-size', '-n', type=int, default=20)
def problem_015(lattice_size):
    """Lattice paths

    Starting in the top left corner of a 2×2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right
    corner.
    
    ![](project/images/p015.gif)
    
    How many such routes are there through a 20×20 grid?
    """

    # You must move right n times and down n times, but it matters not what
    # order.  This is just a permutations of like items
    
    left = lattice_size
    right = lattice_size
    total = left + right

    permutations = factorial(total) // (factorial(left) * factorial(right))

    click.echo(str(permutations))
