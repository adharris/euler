from helpers import get_prime_mask, sieve
from itertools import permutations

limit = 1000000

primes = sieve(limit)
is_prime = get_prime_mask(primes, limit)

def rotate_string(s):
  for i in range(len(s)):
    s = s[1:] + s[0]
    yield s

cycle_primes = []
for p in primes:
  all_prime = True
  for perm in rotate_string(str(p)):
    i = int(''.join(perm))
    all_prime = all_prime & is_prime[i]
  if all_prime:
    cycle_primes.append(p)


print len(cycle_primes)
