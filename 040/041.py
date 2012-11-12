from helpers import cached_prime
from itertools import permutations

def largest_pan_prime(n):
  st = map(lambda x: str(x), range(n, 0, -1))
  perms = map(lambda x: int(''.join(x)), permutations(st))
  primes = filter(cached_prime, perms)
  if len(primes) > 0:
    return max(primes)
  else:
    return []

for i in range(5, 10):
  print (i, largest_pan_prime(i))
