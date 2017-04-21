

import click

@click.command('9')
@click.option('--total', '-t', type=int, default=1000)
def problem_009(total):
    """Special Pythagorean triplet

    A Pythagorean triplet is a set of three natural numbers, a < b < c,
    for which,
    
    a^2 + b^2 = c^2
    
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.  
    Find the product abc.
    
    """

    triples = generate_triples(total)
    triplets = (t for t in triples if is_pythangorean_triplet(*t))
    triple = next(triplets)

    click.echo('{} * {} * {} = {}'.format(
        triple[0],
        triple[1],
        triple[2],
        triple[0] * triple[1] * triple[2],
    ))


def is_pythangorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def generate_triples(total):
    for i in range(1, total):
        for j in range(i + 1, total + 1):
            yield (i, j, total - i - j)