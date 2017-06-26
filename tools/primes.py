
from collections import Counter, defaultdict
from functools import reduce
from itertools import chain, combinations, count
from math import ceil, sqrt
from operator import mul
from random import randint


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


def find_divisors(number, primes):
    factors = []
    for prime in primes:
        count = 0
        while number % prime == 0:
            number //= prime
            factors.append(prime)
    # return factors

    return list(sorted(set(reduce(mul, items, 1) for items in powerset(factors))))


def powerset(iterable):
    return chain.from_iterable(
        combinations(iterable, n) for n in range(len(iterable) + 1))


class PrimeCache(object):
    """A container that can be used to repeatedly factor numbers, reusing the
    calculated prime lists between factorings"""

    def __init__(self, batch=10000):
        self.sieve = unbounded_sieve_of_eratosthenes(batch)
        self.primes = []
        self.prime_set = set()

    def __iter__(self):
        self.ensure_factors_for(10000)
        for i in count():
            if len(self.primes) <= i:
                self.ensure_factors_for(self.primes[-1] + 10000)
            yield self.primes[i]
    
    def factor(self, number):
        self.ensure_factors_for(number)
        factors = factor_with_primes(number, self.primes)
        return factors
        
    def is_prime(self, number):
        self.ensure_factors_for(number)
        return number in self.prime_set

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
            p = next(self.sieve)
            self.primes.append(p)
            self.prime_set.add(p)


def calculate_totient(number, factors):
    # Euler's Product formula:
    # φ(n) = n(1 - 1/p1)(1 - 1/p2)...(1-1/pr)
    # where p1..pr are unique factors of n
    return int(reduce(mul, ((1 - (1 / p)) for p in factors), number))


def sieve_factors(limit):
    factors = defaultdict(tuple)

    for i in range(2, limit + 1):

        # If we haven't seen factors if i, it is prime
        if len(factors[i]) == 0:
            factors[i] = ()
        
            # Normally we can loop starting a n^2, but since we are collecting
            # factors, we need to start at n
            for j in range(i, limit + 1, i):
                factors[j] += (i, )


    return factors



def count_proper_divisors(prime_factors):
    """Returns the number of proper divisors a number has, based on its prime factors"""
    counts = Counter(prime_factors)
    powers = (a + 1 for a in counts.values())
    return reduce(mul, powers, 1)


def miller_rabin_test(number, k):

    if number % 2 == 0:
        return False
        
    r = 1
    while ((number - 1) / 2**r) % 2 == 0:
        r += 1

    d = (number - 1) // 2**r

    print(d, r)
    
    for i in range(k):
        a = randint(2, number - 2)
        x = a**d % number
        
        if x == 1 or x == number - 1:
            continue
        
        for j in range(0, r - 1):
            x = x**2 % number
            if x == 1:
                return False
            if x == number - 1:
                break
            
            if j == r - 2:
                return False
        
    return True


miller_rabin_thresholds = [
    (2047, (2, )),
    (1373653, (2, 3)),
    (9080191, (31, 73)),
    (25326001, (2, 3, 5)),
    (3215031751, (2, 3, 5, 7)),
    (4759123141, (2, 7, 61)),
    (1122004669633, (2, 13, 23, 1662803)),
    (2152302898747, (2, 3, 5, 7, 11)),
    (3474749660383, (2, 3, 5, 7, 11, 13)),
    (341550071728321, (2, 3, 5, 7, 11, 13, 17)),
]


def deterministic_miller_rabin_test(number):
    if number % 2 == 0:
        return False

    a_values = next(t[1] for t in miller_rabin_thresholds if number < t[0])
    
    s, d = miller_rabin_find_r_d(number)
    for a in a_values:

        if mod_base(a, d, number) == 1:
            continue

        for r in range(0, s):
            if mod_base(a, (2**r * d), number) == number - 1:
                break

            if r == s - 1:
                return False
                
    return True


def mod_base(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = base ** 2 % mod
        exp = exp // 2
    return result

def miller_rabin_find_r_d(number):
    r = 1
    while ((number - 1) / 2**r) % 2 == 0:
        r += 1

    d = (number - 1) // 2**r
    return r, d
