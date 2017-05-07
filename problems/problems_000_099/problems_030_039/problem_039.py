

import click

from tools.pythagorean_triples import generate_triples
from collections import Counter


@click.command('39')
@click.option('--limit', '-l', type=int, default=1000)
@click.option('--verbose', '-v', count=True)
def problem_039(limit, verbose):
    """Integer right triangles.

    If _p_ is the perimeter of a right angle triangle with integral length
    sides, {_a_,_b_,_c_}, there are exactly three solutions for _p_ = 120.
    
    {20,48,52}, {24,45,51}, {30,40,50}
    
    For which value of _p_ ≤ 1000, is the number of solutions maximised?
    
    """

    # We could enumerate all triples that sum to < 1000, but there are a bunch
    # of em.  Instead, we can use euclids method to generate primitive triples
    # When we bound m and n of euclids method using the target perimiter, we
    # get much fewer values to try. We do have to check if they are coprime,
    # but this is fast with memoized prime table.  This method runs in reasonble
    # time for perimeters up to 10e5.

    triples = list(generate_triples(limit))
    counted = Counter(sum(triple) for triple in triples)
    most_solutions = counted.most_common(1)[0][0]

    if verbose > 0:
        triples.sort()
        lines = ("{}^2 + {}^2 = {}^2".format(*t) 
                 for t in triples if sum(t) == most_solutions)
        click.echo('\n'.join(lines))
        
    click.echo(most_solutions)
