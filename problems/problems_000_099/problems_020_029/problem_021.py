

import click

from tools.primes import PrimeCache, count_proper_divisors

@click.command('21')
@click.option('--limit', '-l', type=int, default=10000)
def problem_021(limit):
    """Amicable numbers

    Let d(_n_) be defined as the sum of proper divisors of _n_ (numbers less
    than _n_ which divide evenly into _n_).  
    If d(_a_) = _b_ and d(_b_) = _a_, where _a_ ≠ _b_, then _a_ and _b_ are an
    amicable pair and each of _a_ and _b_ are called amicable numbers.
    
    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
    44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
    2, 4, 71 and 142; so d(284) = 220.
    
    Evaluate the sum of all the amicable numbers under 10000.
    """

    cache = AmicableCache()
    numbers = range(2, limit)
    bar = click.progressbar(numbers)
    with bar:
        numbers = [n for n in bar if cache.is_amicable(n)]
    click.echo(sum(numbers))
    

class AmicableCache(object):

    def __init__(self):
        self.primes = PrimeCache()
        self._divisors = {}

    def divisors(self, number):
        if number not in self._divisors: 
            self._divisors[number] = sum(self.primes.proper_divisors(number))
        return self._divisors[number]

    def is_amicable(self, number):
        
        divisors_a = self.divisors(number)
        divisors_b = self.divisors(divisors_a)
        return divisors_b == number and divisors_a != number
    