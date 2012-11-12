from helpers import factor, cached_prime, d_factor
from fractions import gcd
from pprint import pprint
from math import pi, cos

def totient(n):
  f = list(factor(n))
  prod = 1
  for p in f:
    prod *= (1 - float(1) / p)
  return int(round(prod * n))

def totient1(n):
  return sum([ gcd(k, n) * cos( 2 * pi * float(k) / n ) for k in range(1, n +1)])

s = 0
limit = 10**6+1
cached_prime(limit)
for i in range (2, limit):
  s += totient(i)
  if i % 100 == 0: print i
print s 
