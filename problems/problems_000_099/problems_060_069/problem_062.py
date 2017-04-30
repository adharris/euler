

import click
from itertools import permutations, count
from collections import Counter, defaultdict

@click.command('62')
@click.option('--limit', '-l', type=int, default=5)
@click.option('--verbose', '-v', count=True)
def problem_062(limit, verbose):
    """Cubic permutations.

    The cube, 41063625 (345^3), can be permuted to produce two other cubes:
    56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
    cube which has exactly three permutations of its digits which are also
    cube.
    
    Find the smallest cube for which exactly five permutations of its digits
    are cube.
    """

    cube_counts = Counter()
    cubes = defaultdict(set)

    for base in count(1):
        key = "".join(sorted(str(base**3)))
        cube_counts[key] += 1
        cubes[key].add(base)

        if cube_counts[key] >= limit:
            bases = sorted(cubes[key])
            bases = ["{}³ = {}".format(b, b**3) for b in bases]
            click.echo(" ".join(bases))
            break
            