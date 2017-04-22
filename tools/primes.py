
from math import sqrt, ceil
from itertools import count, chain, combinations
from collections import Counter
from operator import mul
from functools import reduce


def sieve_of_eratosthenes(limit):
    """Generate all primes up to limit using a sieve of eratosthenes"""
    primes = []
    visited = [False] * limit
    root_limit = int(sqrt(limit))

    for index in range(2, root_limit + 1):
    
        if not visited[index]:
            visited[index] = True
            primes.append(index)
            for multiple in range(index ** 2, limit, index):
                visited[multiple] = True

    primes.extend(i for i in range(root_limit, limit) if not visited[i])
    
    return primes


def unbounded_sieve_of_eratosthenes(batch_size=1000):
    """Create an infinte generator of primes with an adapted sieve"""
    primes = []
    visited = [False] * batch_size
    
    for index in count(2):

        if index >= len(visited):
            visited.extend([False] * batch_size)
            for prime in primes:
                first_multiple = (index // prime) * prime
                for i in range(first_multiple, len(visited), prime):
                    visited[i] = True

        if not visited[index]:
            visited[index] = True
            primes.append(index)
            yield index
            for multiple in range(index ** 2, len(visited), index):
                visited[multiple] = True


def factor_with_sieve(number):
    """Prime factor a number by generating all primes up to the number and then
    checking each prime against the number"""
    limit = int(ceil(sqrt(number)))
    primes = sieve_of_eratosthenes(limit + 1)
    return factor_with_primes(number, reversed(primes))
    
    
def factor_with_primes(number, primes):
    """Factor a number from a known list of primes"""
    factors = []
    
    for prime in primes:
        while number % prime == 0:
            factors.append(prime)
            number = number / prime

    return factors


class PrimeCache(object):
    """A container that can be used to repeatedly factor numbers, reusing the
    calculated prime lists between factorings"""

    def __init__(self, batch=10000):
        self.sieve = unbounded_sieve_of_eratosthenes(batch)
        self.primes = []
    
    def factor(self, number):
        self.ensure_factors_for(number)
        factors = factor_with_primes(number, self.primes)
        return factors
        
    def is_prime(self, number):
        self.ensure_factors_for(number)
        return number in self.primes

    def count_divisors(self, number):
        primes = self.factor(number)
        return count_proper_divisors(primes)

    def divisors(self, number):
        primes = list(self.factor(number))
        combos = (combinations(primes, n) for n in range(len(primes) + 1))
        powerset = chain.from_iterable(combos)
        return set(reduce(mul, items, 1) for items in powerset)
        
    def proper_divisors(self, number):
        return self.divisors(number) - {number}

    def ensure_factors_for(self, number):
        highest_needed = number
        while len(self.primes) == 0 or self.primes[-1] < highest_needed:
            self.primes.append(next(self.sieve))


def count_proper_divisors(prime_factors):
    """Returns the number of proper divisors a number has, based on its prime factors"""
    counts = Counter(prime_factors)
    powers = (a + 1 for a in counts.values())
    return reduce(mul, powers, 1)