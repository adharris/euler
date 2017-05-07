
from math import floor, sqrt, ceil
from itertools import count

from .primes import sieve_factors
from .memoization import Memoize


# Euclid's method:
# a = k(m^2 - n^2)
# b = k(2mn)
# c = k(m^2 + n^2)
# For coprime m and n and not both odd and any integer k
# a + b + c = m^2 - n^2 + 2mn + m^2 + n^2 = 2m^2 + 2mn
# so we only need n, m such that 2m^2 + 2mn < 1000
# We can solve for n: n < (1000 - 2m^2) / 2m
# Since n must be > 0, we can bound n:
# 0 < (1000 - 2m^2) / 2m => 2m^2 < 1000 => m < sqrt(1000/2)


def generate_triples(perimeter_limit, factors=None):

    if factors is None:
        factors = sieve_factors(int(perimeter_limit / 2) + 1)
        
    for m, n in generate_triple_bases(perimeter_limit, factors):
        yield from generate_triples_from_base(m, n, perimeter_limit)


def generate_triple_bases(perimeter_limit, factors):

    for m in range(1, m_upper_bound(perimeter_limit)):
        for n in range(1, n_upper_bound(m, perimeter_limit)):
            if is_triple_base(m, n, factors):
                yield (m, n)


def is_triple_base(m, n, factors):
    return (m % 2 == 0 or n % 2 == 0) \
        and m > n and n > 0 \
        and are_coprime(m, n, factors)


@Memoize(arg_count=2)
def are_coprime(m, n, factors):
    m_factors = set(factors[m])
    n_factors = set(factors[n])
    return len(m_factors & n_factors) == 0


def m_upper_bound(perimeter_limit):
    return int(floor(sqrt(perimeter_limit / 2)))


def n_upper_bound(m, perimeter_limit):
    return int(ceil((perimeter_limit - 2 * m ** 2) / (2 * m)))


def generate_triples_from_base(m, n, perimeter_limit):
    for k in count(1):
        triple = calculate_triple(m, n, k)
        if sum(triple) > perimeter_limit:
            return
        yield triple


def calculate_triple(m, n, k=1):
    return (
        calculate_a(m, n, k), 
        calculate_b(m, n, k), 
        calculate_c(m, n, k))


def calculate_a(m, n, k=1):
    return k * (m**2 - n**2)


def calculate_b(m, n, k=1):
    return k * 2 * m * n


def calculate_c(m, n, k=1):
    return k * (m**2 + n**2)

