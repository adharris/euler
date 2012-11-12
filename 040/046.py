from math import sqrt
from helpers import cached_prime

def lower_twice_squares(n):
  i = 1
  while i**2 * 2 < n:
    yield i**2 * 2
    i += 1

def is_goldbach(n):
  for sq in lower_twice_squares(n):
    if cached_prime(n - sq):
      return True
  return False


cached_prime(100000)
i = 3
while True:
  if not cached_prime(i) and not is_goldbach(i):
    print i
    break
  i += 2
