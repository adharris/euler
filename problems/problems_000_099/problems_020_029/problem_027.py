

import click

from itertools import count, product, islice
from tools.primes import PrimeCache


@click.command('27')
@click.option('--limit', '-l', type=int, default=1000)
def problem_027(limit):
    """Quadratic primes

    Euler discovered the remarkable quadratic formula:
    
    $n^2 + n + 41$
    
    It turns out that the formula will produce 40 primes for the consecutive
    integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 =
    40(40 + 1) + 41$ is divisible by 41, and certainly when $n = 41, 41^2 + 41
    + 41$ is clearly divisible by 41.
    
    The incredible formula $n^2 - 79n + 1601$ was discovered, which produces
    80 primes for the consecutive values $0 \le n \le 79$. The product of the
    coefficients, −79 and 1601, is −126479.
    
    Considering quadratics of the form:
    
    > $n^2 + an + b$, where $|a| &lt; 1000$ and $|b| \le 1000$  
    >  
    >
    
    >
    
    > where $|n|$ is the modulus/absolute value of $n$  
    > e.g. $|11| = 11$ and $|-4| = 4$
    
    Find the product of the coefficients, $a$ and $b$, for the quadratic
    expression that produces the maximum number of primes for consecutive
    values of $n$, starting with $n = 0$.
    
    """

    primes = PrimeCache()
    pairs = product(range(-limit + 1, limit), range(-limit, limit + 1))
    series = ((a, b, prime_count(primes, create_series(a, b))) for a, b in pairs)
    series = (s for s in series if s[2] >= 0)
    longest = max(series, key=lambda s: s[2])
    
    click.echo(longest[0] * longest[1])

def prime_count(primes, series):
    not_prime = (i for i, p in enumerate(series) if not primes.is_prime(p))
    return next(not_prime) - 1


def create_series(a, b):
    for n in count():
        yield n**2 + a * n + b
