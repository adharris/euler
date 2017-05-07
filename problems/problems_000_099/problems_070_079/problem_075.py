
import click

from collections import Counter

from tools.pythagorean_triples import generate_triples

@click.command('75')
@click.option('--limit', '-l', type=int, default=1500000)
@click.option('--verbose', '-v', count=True)
def problem_075(limit,verbose):
    """Singular integer right triangles.

    It turns out that 12 cm is the smallest length of wire that can be bent to
    form an integer sided right angle triangle in exactly one way, but there
    are many more examples.
    
    **12 cm**: (3,4,5)  
    **24 cm**: (6,8,10)  
    **30 cm**: (5,12,13)  
    **36 cm**: (9,12,15)  
    **40 cm**: (8,15,17)  
    **48 cm**: (12,16,20)
    
    In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
    integer sided right angle triangle, and other lengths allow more than one
    solution to be found; for example, using 120 cm it is possible to form
    exactly three different integer sided right angle triangles.
    
    **120 cm**: (30,40,50), (20,48,52), (24,45,51)
    
    Given that L is the length of the wire, for how many values of L ≤
    1,500,000 can exactly one integer sided right angle triangle be formed?
    
    """

    triples = generate_triples(limit)
    perimeters = Counter(sum(triple) for triple in triples)
    only_one = sum(1 for c in perimeters.values() if c == 1)
    print(only_one)