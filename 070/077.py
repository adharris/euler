from helpers import cached_prime, all_factors, is_prime, prime_gen, factor, memoized

def combos(N, less_than = None):
  if less_than is None: less_than = N
 
def a_n(n):
  if n == 1: return 0
  elif is_prime(n): return 1
  else: return 0

@memoized
def c_n(n):
  return sum(factor(n).keys())

@memoized
def b_n(n):
  return (c_n(n) + sum([c_n(k) * b_n(n-k) for k in range(1, n)])) / n 

def first_n_partitions(n):
  cached_prime(10**6)
  i = 0
  while True:
    i += 1
    if b_n(i) >= n:
      return i
    if i % 1000 == 0: print i

print first_n_partitions(5000)
