

import click

from collections import namedtuple, defaultdict
from tools.pythagorean_triples import generate_triples
from math import sqrt
from itertools import count

@click.command('86')
@click.option('--limit', '-l', type=int, default=1000000)
@click.option('--verbose', '-v', count=True)
def problem_086(limit,verbose):
    """Cuboid route.

    A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3,
    and a fly, F, sits in the opposite corner. By travelling on the surfaces
    of the room the shortest "straight line" distance from S to F is 10 and
    the path is shown on the diagram.
    
    ![](project/images/p086.gif)  
    
    However, there are up to three "shortest" path candidates for any given
    cuboid and the shortest route doesn't always have integer length.
    
    It can be shown that there are exactly 2060 distinct cuboids, ignoring
    rotations, with integer dimensions, up to a maximum size of M by M by M,
    for which the shortest route has integer length when M = 100. This is the
    least value of M for which the number of solutions first exceeds two
    thousand; the number of solutions when M = 99 is 1975.
    
    Find the least value of M such that the number of solutions first exceeds
    one million.
    
    """

    # Three routes:
    #         *------F        Sides labeled A, B, C, routes clockwise from S
    #         |     /|        R1^2 = (A + C)^2 + B^2
    #         |    / n        R2^2 = (B + C)^2 + A^2
    #   +-----+------+-----F  R3^2 = (A + B)^2 + C^2
    #   |     |  /   |  . `|
    #   |     A /   .|`  / |
    #   |     |/. ` a-n /  |
    #   +-C---S-b-B--+-----+
    #         | ` .  |
    #         |     `|
    #         *------+
    #         |      |
    #         |      |
    #         |      |
    #         +------F
    
    # Genreate all triples up to perimeter 3M + sqrt((M + M)^2 + M^2)
    # Which is is 3M + sqrt(5M^2)

    total_found = 0
    cuboids = defaultdict(set)
    triples = set()
    under_length = []
    
    for batch in count():
        size = (batch + 1) * 500
        max_triple_perimeter = int(3 * size + sqrt(5 * size**2)) + 1
        all_triples = set(generate_triples(max_triple_perimeter))
        this_loop = all_triples - triples
        triples = all_triples
        
        with click.progressbar(this_loop, label="{}".format(total_found)) as bar:
            new_cuboids = (c for t in bar for c in generate_cuboids(t))
            new_cuboids = (c for c in new_cuboids if c.a > 0)
            new_cuboids = (c for c in new_cuboids if is_shortest_route_integral(c))
            for cuboid in new_cuboids:
                cuboids[cuboid.c].add(cuboid)
                
        for i in range(batch * 500, batch * 500 + 500):
        
            total_found += len(cuboids[i])
            if total_found >= limit:
                click.echo(total_found)
                click.echo(i)
                return


class Cuboid(namedtuple('Cuboid', 'a b c')):

    def __new__(cls, *args):
        return super(Cuboid, cls).__new__(cls, *sorted(args))


def generate_cuboids(triple):
    # Hold the smallest size constant, and split the larger

    # Want to generate cubes with route 1 being the triple until route 2 or 3
    # becomes longer
    
    for a in range(1, triple[1]):
        yield Cuboid(a, triple[1] - a, triple[0])
    
    for a in range(1, triple[0]):
        yield Cuboid(a, triple[0] - a, triple[1])



def is_shortest_route_integral(cuboid):
    shortest = shortest_route(cuboid)
    return int(shortest) == shortest


def shortest_route(cuboid):
    return min(
        route_1_length(cuboid),
        route_2_length(cuboid),
        route_3_length(cuboid))

def route_1_length(cuboid):
    return sqrt((cuboid.a + cuboid.c)**2 + cuboid.b**2)


def route_2_length(cuboid):
    return sqrt((cuboid.b + cuboid.c)**2 + cuboid.a**2)


def route_3_length(cuboid):
    return sqrt((cuboid.a + cuboid.b)**2 + cuboid.c**2)
    
