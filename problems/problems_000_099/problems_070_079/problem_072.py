

import click


from tools.primes import sieve_factors, calculate_totient


@click.command('72')
@click.option('--limit', '-l', type=int, default=1000000)
@click.option('--verbose', '-v', count=True)
def problem_072(limit,verbose):
    """Counting fractions.

    Consider the fraction, _n/d_, where _n_ and _d_ are positive integers. If
    _n_&lt;_d_ and HCF(_n,d_)=1, it is called a reduced proper fraction.
    
    If we list the set of reduced proper fractions for _d_ ≤ 8 in ascending
    order of size, we get:
    
    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
    5/7, 3/4, 4/5, 5/6, 6/7, 7/8
    
    It can be seen that there are 21 elements in this set.
    
    How many elements would be contained in the set of reduced proper
    fractions for _d_ ≤ 1,000,000?
    
    """

    # Fractions are reduced if GCD(N, D) = 1. So N/D are coprime. So the number
    # of such fractions for any given D is φ(D).  So there are sum(φ(D)) for
    #  D < limit number of fractions

    factors = sieve_factors(limit)
    totients = [(n, calculate_totient(n, f)) for n, f in factors.items()]
    click.echo(sum(φ for _, φ in totients))
