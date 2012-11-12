from helpers import global_primes, cached_prime
from math import log

limit = 10000000
cached_prime(limit)
primes = global_primes()
known_max = 11

def trunk_left(n):
  p = int(log(n, 10))
  return n % 10**p
def trunk_right(n):
  return n / 10

def truncations(n):
  l = n
  while l >= 10:
    l = trunk_left(l)
    yield l
  r = n
  while r >= 10:
    r = trunk_right(r)
    yield r

match = []
for p in primes:
  if p < 10:
    continue
  t = list(truncations(p))
  f = filter(cached_prime, t)
  if len(t) == len(f):
    match.append(p)
    print (p, t)
    if len(match) >= known_max:
      break

print sum(match)
