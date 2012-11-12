from math import sqrt
from helpers import cached_prime, prime_gen, factor

def totient(n, f):
  prod = 1
  for p in f:
    prod *= (1 - float(1) / p)
  return int(round(prod * n))

def is_perm(n1, n2):
  return sorted(str(n1)) == sorted(str(n2))

limit = 10**7
primes = list(prime_gen(max_size = limit/2 ))

m = limit
for p in reversed(primes):
  for p2 in primes:
    if p*p2 > limit:
      break
    t = totient(p*p2, (p, p2))
    if is_perm(p*p2, t):
      if m > float(p)*p2/t:
        m = float(p)*p2/t
        print(p*p2, t, float(p)*p2/t)

