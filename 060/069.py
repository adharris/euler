from helpers import factor, cached_prime, prime_gen
from math import sqrt

def totient(n):
  f = factor(n)
  prod = 1
  for p in f:
    prod *= (1 - float(1) / p)
  return int(round(prod * n))

limit = 1000000
cached_prime(1000000)
prod = 1
for p in prime_gen():
  prod *= p
  if prod <= limit:
    t = totient(prod)
    print (prod, t, float(prod) / t)
  else:
    break
