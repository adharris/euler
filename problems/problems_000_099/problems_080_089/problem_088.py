

import click

from tools.primes import find_divisors, sieve_factors
from bisect import bisect_right
from itertools import combinations

@click.command('88')
@click.option('--limit', '-l', type=int, default=12000)
@click.option('--verbose', '-v', count=True)
def problem_088(limit, verbose):
    """Product-sum numbers.

    A natural number, N, that can be written as the sum and product of a given
    set of at least two natural numbers, {_a_1, _a_2, ... , _a__k_} is called
    a product-sum number: N = _a_1 \+ _a_2 \+ ... + _a__k_ = _a_1 × _a_2 × ...
    × _a__k_.
    
    For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.
    
    For a given set of size, _k_, we shall call the smallest N with this
    property a minimal product-sum number. The minimal product-sum numbers for
    sets of size, _k_ = 2, 3, 4, 5, and 6 are as follows.
    
    _k_=2: 4 = 2 × 2 = 2 + 2  
    _k_=3: 6 = 1 × 2 × 3 = 1 + 2 + 3  
    _k_=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4  
    _k_=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2  
    _k_=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6
    
    Hence for 2≤_k_≤6, the sum of all the minimal product-sum numbers is
    4+6+8+12 = 30; note that 8 is only counted once in the sum.
    
    In fact, as the complete set of minimal product-sum numbers for 2≤_k_≤12
    is {4, 6, 8, 12, 15, 16}, the sum is 61.
    
    What is the sum of all the minimal product-sum numbers for 2≤_k_≤12000?
    
    """

    factors = sieve_factors(limit * 2)
    divisors = {n: find_divisors(n, f) for n, f in factors.items()}
    
    
    k_values = {}
    values_to_find = limit - 1

    with click.progressbar(range(2, limit * 2)) as bar:
    
        for number in bar:
            products = enumerate_products(number, divisors)
            products = (p for p in products if len(p) > 1)
            products = set(tuple(sorted(p)) for p in products)
            
            for product in products:
                k = len(product) + number - sum(product)
                if k <= limit and k not in k_values:
                    k_values[k] = number
                    values_to_find -= 1
                
                    if values_to_find == 0:
                        break
    
            if values_to_find == 0:
                break
                
    values = set(k_values.values())
    click.echo(sum(values))

def find_product_sums(number, divisors):
    products = enumerate_products(number, divisors)
    products = (p for p in products if len(p) > 1)
    products = set(tuple(sorted(p)) for p in products)
    if len(products):
        return min(products, key=sum)



def enumerate_products(number, divisors, limit=None):
    yield (number, )
    
    if limit:
        start = bisect_right(divisors[number], limit) - 1
    else:
        start = 1

    for i, divisor in enumerate(divisors[number][1:-start][::-1]):
        for sub_product in enumerate_products(number // divisor, divisors, divisor):
            yield (divisor, ) + sub_product


def partition_a(collection):
    for count in range(1, len(collection) - 1):
        for indices in combinations(range(0, len(collection) - 1), count):
            yield [collection[i] for i in indices]

def generate_partitions(collection):

    if len(collection) == 1:
        yield (tuple(collection), ) 
        return
    
    first = collection[0]

    for smaller in generate_partitions(collection[1:]):
        print('smaller', smaller)

        for i, subset in enumerate(smaller):
            yield smaller[:i] + (((first, ) + subset), ) + smaller[i + 1:]

        yield (((first), ), ) + smaller


def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller