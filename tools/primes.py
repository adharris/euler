
from math import sqrt, ceil
from itertools import count

def sieve_of_eratosthenes(limit):
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
    limit = int(ceil(sqrt(number)))
    primes = sieve_of_eratosthenes(limit + 1)
    return factor_with_primes(number, reversed(primes))
    
    
def factor_with_primes(number, primes):
    factors = []
    
    for prime in primes:
        while number % prime == 0:
            factors.append(prime)
            number = number / prime

    return factors