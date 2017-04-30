

import click

@click.command('48')
@click.option('--limit', '-l', type=int, default=1000)
@click.option('--verbose', '-v', count=True)
def problem_048(limit,verbose):
    """Self powers.

    The series, 11 \+ 22 \+ 33 \+ ... + 1010 = 10405071317.
    
    Find the last ten digits of the series, 11 \+ 22 \+ 33 \+ ... + 10001000.
    
    """

    total = sum(i**i for i in range(1, limit + 1))
    click.echo(str(total)[-10:])