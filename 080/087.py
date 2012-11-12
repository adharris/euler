from helpers import prime_gen
from math import sqrt

def below(M):
  m = int(sqrt(M - (2**3 + 2**4)))
  print "need primes less than %s" % m
  primes = list(prime_gen(max_size = m))

  nums = set([])
  for p1 in primes:
    if p1**2 + 2**3 + 2**4 > M:
      break
    for p2 in primes:
      if p1**2 + p2**3 + 2**4 > M:
        break
      for p3 in primes:
        if p1**2 + p2**3 + p3**4 > M:
          break
        nums.add(p1**2+p2**3+p3**4)
  return len(nums)


print below(50000000)
